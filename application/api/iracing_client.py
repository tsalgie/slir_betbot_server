#!python3
from flask import current_app as app

GRID = 0
LIGHTS_OUT = 1
FINISHED = 2
SESSION_DONE = 3
CRASHED = 3


def irsdk():
    app.config['IR']


def field_size():
    pass


def car_position():
    #standings().index(app.config['IRACING_USER'])  # 0 indexed
    pass


def car_status():
    pass


def elapsed_laps():
    pass


def elapsed_seconds():
    pass


def session():
    pass


def session_status():
    pass


def timed_race():
    pass


def total_race_laps():
    pass


def total_race_time():
    pass
