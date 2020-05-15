from flask import Flask, render_template,request,redirect,flash,send_from_directory
from werkzeug.utils import secure_filename
import requests
import os
import sys
# sys.path.append("myspa")
# import BuildLane



UPLOAD_FOLDER = '/Users/yoshimasa/projects/myspa/backend/uploads/'

app = Flask(__name__, template_folder='./templates')
app.config["SECRET_KEY"] = "sample"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)