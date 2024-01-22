import os

from flask import Flask


app = Flask(__name__)


app.config['MAX_CONTENT_LENGTH'] = 20 * 1024 * 1024

app.config['ALLOWED_EXSTENSIONS'] = {'png'}
app.config['CONVERT_FOLDER'] = 'app/static/convert'
app.config['UPLOAD_FOLDER'] = 'app/static/uploads'

from . import routes