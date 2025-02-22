from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/generate", methods=["POST"])
def generate():
    return # Processed Pic