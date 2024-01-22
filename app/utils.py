from . import app


def checkExstension(filename):
    return filename.split('.')[-1] in app.config['ALLOWED_EXSTENSIONS']
