from flask import send_file
from app import app

@app.route("/cv")
def index():
    return send_file("templates/cv.html")
