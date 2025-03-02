from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from PIL import Image
import os
from datetime import datetime
from Algorithm.addPattern import add_hatches_to_bars

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

@app.route("/")
def hello_world():
    return "Connection Successful"


# def receive_file():
#     if "file" not in request.files:
#         return jsonify({"error": "No file part"}), 400
#
#     file = request.files["file"]
#
#     if file.filename == "":
#         return jsonify({"error": "No selected file"}), 400
#
#     # Extract file extension
#     file_ext = os.path.splitext(file.filename)[1]
#
#     # Generate a new file name with timestamp
#     new_filename = datetime.now().strftime("%Y%m%d%H%M%S") + file_ext
#
#     # Save file
#     file_path = os.path.join(app.config["UPLOAD_FOLDER"], new_filename)
#     file.save(file_path)
#
#     return file_path


@app.route("/addpattern/", methods=["POST"])
@app.route("/addpattern/<color>", methods=["POST"])
def add_pattern(color=None):
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

    # process image
    output_path = os.path.join(app.config["OUTPUT_FOLDER"], new_filename)
    if color is None:
        add_hatches_to_bars(file_path, output_path)

    # send file back, need path to the processed pic
    if os.path.exists(output_path):
        return send_file(output_path)


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

