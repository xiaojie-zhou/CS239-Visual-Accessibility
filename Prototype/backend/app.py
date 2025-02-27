from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
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

@app.route("/generate", methods=["POST"])
def generate():
    """assuming uploaded in FormData"""
    # TODO: Convert img if needed
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

    # todo: process image
    output_path = os.path.join(app.config["OUTPUT_FOLDER"], new_filename)
    add_hatches_to_bars(file_path, output_path)

    # send file back, need path to the processed pic
    if os.path.exists(output_path):
        return send_file(output_path)


def convert():
    return
