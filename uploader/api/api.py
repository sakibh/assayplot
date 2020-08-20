import os
from flask import Flask, jsonify, request, session
from werkzeug.utils import secure_filename
from flask_cors import CORS
from pathlib import Path

ROOT_PATH = Path.cwd().parent
UPLOAD_FOLDER = f'{ROOT_PATH}/uploads'
RESULTS_FOLDER = f'{ROOT_PATH}/results'
ALLOWED_EXTENSIONS = set(['txt', 'csv'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app)


@app.route('/upload', methods=['POST'])
def uploadData():
    target = os.path.join(UPLOAD_FOLDER, )
    if not os.path.isdir(target):
        os.mkdir(target)
    file = request.files['file']
    filename = secure_filename(file.filename)
    destination = "/".join([target, filename])
    file.save(destination)
    session['uploadFilePath'] = destination
    response = "Success!"
    return response

@app.route('/data', methods=['GET'])
def getData():
    return "Data"

if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run(debug=True,host="0.0.0.0",use_reloader=False)