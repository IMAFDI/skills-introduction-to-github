"""
Simple Flask app to view a local image in the browser.
Place an image named `image.jpg` in the same folder, then run:

    pip install flask
    python view_image.py

Open http://localhost:8000 in your browser.
"""
from flask import Flask, send_file, abort
import os
import mimetypes

app = Flask(__name__)
IMAGE_NAME = "image.jpg"

@app.route("/")
def index():
    if not os.path.exists(IMAGE_NAME):
        return (
            "<p>No image found. Place an image named <strong>image.jpg</strong> "
            "in this folder and refresh.</p>"
        )
    return (
        "<html><body><h3>Image Preview</h3>"
        "<img src=\"/image\" style=\"max-width:100%;height:auto\"/>"
        "</body></html>"
    )

@app.route("/image")
def image():
    if not os.path.exists(IMAGE_NAME):
        abort(404)
    mime = mimetypes.guess_type(IMAGE_NAME)[0] or "application/octet-stream"
    return send_file(IMAGE_NAME, mimetype=mime)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
