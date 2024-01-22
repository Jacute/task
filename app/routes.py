from . import app
from flask import render_template, request, send_file, jsonify, send_from_directory
from .utils import checkExstension

import os
import subprocess


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert')
def convertImage():
    file = request.args.get('file')
    if file:
        new_filename = file.split(".")[0] + '.jpg'
        
        input_filepath = os.path.join(app.config["UPLOAD_FOLDER"], file)
        output_filepath = os.path.join(app.config["CONVERT_FOLDER"], new_filename)
        
        command = f'convert {input_filepath} {output_filepath}'
        print(command)
        
        
        try:
            result = subprocess.check_output(command, shell=True)
            status = "OK"
            message = f'Your file was successfully converted. \n {result}'
        except Exception as e:
            status = "BAD"
            message = f'Something went wrong. Error: {e}'
        
        response_data = {
            "status": status,
            "message": message,
            "converted_file": new_filename
        }
        
        return jsonify(response_data)
        
    files = os.listdir(os.path.join(app.config['UPLOAD_FOLDER']))
    return render_template('convert.html', files=files)


@app.route('/convert/<string:file>')
def getImage(file):
    if file:
        return send_file(os.path.join('static/convert', file), mimetype='image/jpeg')

@app.route('/upload', methods=['POST'])
def convert():
    if 'image' not in request.files:
        message = "File not uploaded"
        status = "BAD"
    else:
    
        file = request.files['image']
        
        if file.filename == '':
            message = "File not uploaded"
            status = "BAD"
        else:
        
            if file and checkExstension(file.filename):
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
                try:
                    file.save(filepath)
                except:
                    status = "BAD"
                    message = "File can't be saved"
                
                status = "OK"
                message = f"Image {file.filename} successfully uploaded"
            else:
                status = "BAD"
                message = "File should be image"
                
    response_data = {
            "status": status,
            "message": message,
            "uploaded_file": file.filename
        }

    return jsonify(response_data)

