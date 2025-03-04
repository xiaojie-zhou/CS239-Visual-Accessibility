from flask import Flask, request, jsonify, send_file, url_for
from flask_cors import CORS
from PIL import Image
import os
from datetime import datetime
from Algorithm.addPattern import add_hatches_to_bars
import uuid
from Algorithm.simulate_colorblind import simulate_colorblind

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
        return jsonify({"error": "No file part"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

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
        return jsonify({"error": "Upload os path non-exist."}), 500

def is_valid_image(file_path):
    """Check if the file is a real image"""
    try:
        img = Image.open(file_path)
        img.verify()
        return True
    except (IOError, SyntaxError):
        return False
    
def convert_to_png(image_path):
    """Convert any image to PNG format"""
    new_path = os.path.splitext(image_path)[0] + ".png"
    with Image.open(image_path) as img:
        img.convert("RGBA").save(new_path, "PNG")
    return new_path

@app.route("/clear", methods=["POST"])
def clear():
    # Clear the uploaded folder
    for file in os.listdir(app.config["UPLOAD_FOLDER"]):
        os.remove(os.path.join(app.config["UPLOAD_FOLDER"], file))
    # Clear the output folder # no need to clear outputs bc they are not generated yet
    # for file in os.listdir(app.config["OUTPUT_FOLDER"]):
    #     os.remove(os.path.join(app.config["OUTPUT_FOLDER"], file))

    file_store.clear()
    return jsonify({"message": "All files cleared."}), 200

@app.route("/getImg", methods=["GET"])
def get_image():
    token = request.args.get("token")
    if token not in file_store:
        return jsonify({"error": "Invalid token"}), 400
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], file_store[token]+".png")

    color = request.args.get("color")
    # ['normal', 'prot', 'deut', 'trit', 'gray']
    if color is not None and color not in ['normal', 'prot', 'deut', 'trit', 'gray']:
        return jsonify({"error": "Invalid color"}), 400

    if color is None: #retrieve the original copy for uploader rendering
        if not os.path.exists(file_path):
            return jsonify({"error": "File not found"}), 404
        return send_file(file_path, mimetype="image/png"), 200
    else: # TODO: retrieve the processed image
        return jsonify({"error": "TODO"}), 400

    # if color is None:
    #     add_hatches_to_bars(file_path, app.config["OUTPUT_FOLDER"])
    #     output_path = os.path.join(app.config["OUTPUT_FOLDER"], file_store[token]+"_hatched_bars.png")

    # if os.path.exists(output_path):
    #     return send_file(output_path), 200
    # else:
    #     print(output_path)
    #     return jsonify({"error": "Image not generated."}), 500

@app.route("/simulate", methods=["GET"])
def simulate():
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


