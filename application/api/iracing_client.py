#!python3
from flask import current_app as app


def irsdk():
    app.config['IR']