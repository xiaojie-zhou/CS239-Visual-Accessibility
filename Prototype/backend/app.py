from flask import Flask, request, jsonify, send_file, url_for
from flask_cors import CORS
from PIL import Image
import os
from datetime import datetime
from Algorithm.addPattern import add_hatches_to_bars
import uuid
from Algorithm.simulate_colorblind import simulate_colorblind
from Algorithm.evaluateFigure import evaluate_graph

app = Flask(__name__)
CORS(app)

# Define the upload directory
UPLOAD_FOLDER = os.path.join(os.getcwd(), "user_input")  # Saves in the current project directory
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Ensure the folder exists
# Define the output directory
OUTPUT_FOLDER = os.path.join(os.getcwd(), "output")  # Saves in the current project directory
os.makedirs(OUTPUT_FOLDER, exist_ok=True)  # Ensure the folder exists
# Define the simulated directory
SIMULATED_FOLDER = os.path.join(os.getcwd(), "simulation")  # Saves in the current project directory
os.makedirs(SIMULATED_FOLDER, exist_ok=True)  # Ensure the folder exists

# Configure Flask to use this directory for uploaded files
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["OUTPUT_FOLDER"] = OUTPUT_FOLDER
app.config["SIMULATED_FOLDER"] = SIMULATED_FOLDER

# Store the uploaded file paths in memory
# {token: file_name}
file_store = {}

@app.route("/")
def hello_world():
    return "Backend Online", 200


@app.route("/upload", methods=["POST"])
def upload():
# def upload(color=None):
    """assuming uploaded in FormData"""
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded. Frontend did send request without file"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "No selected file. Wouldn't happen unless misusing"}), 400

    # Extract file extension
    file_ext = os.path.splitext(file.filename)[1]

    # Generate a new file name with timestamp
    new_filename = datetime.now().strftime("%Y%m%d%H%M%S")

    # Save file
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], new_filename+file_ext)
    file.save(file_path)

    # Validate the image
    if not is_valid_image(file_path):
        os.remove(file_path)
        return jsonify({"error": "Invalid or corrupted image file."}), 400
    
    # Convert to PNG if needed
    if file_ext != ".png":
        file_path = convert_to_png(file_path)

    if os.path.exists(file_path):
        token = uuid.uuid4().hex
        file_store[token] = new_filename
        return jsonify({"image": token}), 200
    else:
        return jsonify({"error": "Upload os path non-exist. Backend error."}), 500

def is_valid_image(file_path):
    """Check if a file is a valid and readable image."""
    try:
        with Image.open(file_path) as img:
            img.verify()  # Quick check for file integrity
            img = Image.open(file_path)  # Reopen because verify() leaves the image in an unusable state
            img.load()  # Load full image to ensure it's not corrupted
        return True
    except (IOError, SyntaxError):
        return False

def convert_to_png(image_path):
    """Convert any image to PNG format"""
    new_path = os.path.splitext(image_path)[0] + ".png"
    with Image.open(image_path) as img:
        img.convert("RGBA").save(new_path, "PNG")
    os.remove(image_path)  # Delete original file
    return new_path

@app.route("/get-preview", methods=["GET"])
def get_preview():
    token = request.args.get("token")
    if token not in file_store:
        return jsonify({"error": "Invalid token"}), 400
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], file_store[token]+".png")
    if os.path.exists(file_path):
        return send_file(file_path), 200
    else:
        return jsonify({"error": "Token available, but image not found. This should not happen"}), 404

@app.route("/clear", methods=["POST"])
def clear():
    # Clear the uploaded folder but keep .gitignore
    for file in os.listdir(app.config["UPLOAD_FOLDER"]):
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], file)
        if file != ".gitignore":  # Skip .gitignore
            os.remove(file_path)

    # Below are not in the workflow, but for our own convenience
    # Clear the output folder but keep .gitignore
    for file in os.listdir(app.config["OUTPUT_FOLDER"]):
        file_path = os.path.join(app.config["OUTPUT_FOLDER"], file)
        if file != ".gitignore":
            os.remove(file_path)

    # Clear the simulated folder but keep .gitignore
    for file in os.listdir(app.config["SIMULATED_FOLDER"]):
        file_path = os.path.join(app.config["SIMULATED_FOLDER"], file)
        if file != ".gitignore":
            os.remove(file_path)

    file_store.clear()
    return jsonify({"message": "All files cleared."}), 200

@app.route("/get-result", methods=["GET"])
def get_result():
    token = request.args.get("token")
    if token not in file_store:
        return jsonify({"error": "Invalid token"}), 400
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], file_store[token]+".png")

    color = request.args.get("color")
    # ['default', 'prot', 'deut', 'trit', 'gray']
    if color is None:
        color = "normal"
    if color not in ['normal', 'prot', 'deut', 'trit', 'gray']:
        return jsonify({"error": "Invalid color. Frontend bad request"}), 400

    try:
        add_hatches_to_bars(file_path, app.config["OUTPUT_FOLDER"], color_palette=color)
    except Exception as e:
        return jsonify({"error": f"Failed to generate image: {str(e)}"}), 500

    hatch = request.args.get("hatch")
    if hatch == "False":
        output_path = os.path.join(app.config["OUTPUT_FOLDER"], file_store[token] + "_color_adjusted.png")
    else:
        output_path = os.path.join(app.config["OUTPUT_FOLDER"], file_store[token] + "_hatched_bars.png")

    if os.path.exists(output_path):
        return send_file(output_path), 200
    else:
        print(output_path)
        return jsonify({"error": "Image not generated. Should not happen."}), 500

@app.route("/get-simulation", methods=["GET"])
def get_simulation():
    # require: ?token= & color=
    # color: ['prot', 'deut', 'trit']
    token = request.args.get("token")
    if token not in file_store:
        return jsonify({"error": "Invalid token"}), 400
    base_filename = file_store[token]

    color = request.args.get("color")
    if color not in ['prot', 'deut', 'trit']:
        return jsonify({"error": "Invalid color"}), 400

    simulated_folder = app.config["SIMULATED_FOLDER"]
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], base_filename + ".png")

    simulate_colorblind(file_path, output_folder=app.config["SIMULATED_FOLDER"])

    # Paths of generated images
    simulated_images = {
        "prot": os.path.join(simulated_folder, f"{base_filename}_PROTAN.png"),
        "deut": os.path.join(simulated_folder, f"{base_filename}_DEUTAN.png"),
        "trit": os.path.join(simulated_folder, f"{base_filename}_TRITAN.png"),
    }
    # Check if all simulated images exist
    for key, path in simulated_images.items():
        if not os.path.exists(path):
            return jsonify({"error": f"Simulation failed for {key}"}), 500

    return send_file(simulated_images[color], mimetype="image/png"), 200

@app.route("/get-score", methods=["GET"])
def get_score():
    # require: ?token=
    token = request.args.get("token")
    if token not in file_store:
        return jsonify({"error": "Invalid token"}), 400
    file_path = os.path.join(UPLOAD_FOLDER, file_store[token]+".png")

    try:
        score = evaluate_graph(file_path)
        return jsonify({"score": score}), 200
    except Exception as e:
        return jsonify({"error": f"Failed to evaluate graph: {str(e)}"}), 500



