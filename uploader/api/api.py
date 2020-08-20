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

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/api/upload', methods=['POST'])
def uploadData():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print('No file selected')
            return 'No file selected'
        file = request.files['file']
        plot_title = request.form["title"]
        if file.filename == '':
            print('No file selected for uploading')
            return 'No files selected'
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print('File successfully uploaded')
            print(plot_title)
            return 'Success!'
        else:
            print('Allowed file types: txt, csv')
            return 'Try again!'

@app.route('/api/data', methods=['GET'])
def getData():
    return "Data"

if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run(debug=True,host="0.0.0.0",use_reloader=False)