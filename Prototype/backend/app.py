from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from PIL import Image
import os
from datetime import datetime
from Algorithm.addPattern import add_hatches_to_bars
import uuid

app = Flask(__name__)
CORS(app)

# Define the upload directory
UPLOAD_FOLDER = os.path.join(os.getcwd(), "user_input")  # Saves in the current project directory
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Ensure the folder exists
# Define the output directory
OUTPUT_FOLDER = os.path.join(os.getcwd(), "output")  # Saves in the current project directory
os.makedirs(OUTPUT_FOLDER, exist_ok=True)  # Ensure the folder exists

# Configure Flask to use this directory for uploaded files
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["OUTPUT_FOLDER"] = OUTPUT_FOLDER

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
    new_filename = datetime.now().strftime("%Y%m%d%H%M%S") + file_ext

    # Save file
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], new_filename)
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

@app.route("/getImg/<token>/<color>", methods=["GET"])
def get_image(token, color=None):
    # process image and save
    if token not in file_store:
        return jsonify({"error": "Invalid token"}), 400

    output_path = os.path.join(app.config["OUTPUT_FOLDER"], file_store[token])
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], file_store[token])

    # TODO: Add color processing
    if color is None:
        add_hatches_to_bars(file_path, output_path)

    if os.path.exists(output_path):
        return jsonify(send_file(output_path)), 200
    else:
        return jsonify({"error": "Image not generated."}), 500


