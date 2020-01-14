#!python3
from flask import current_app as app

GRID = 0
LIGHTS_OUT = 1
FINISHED = 2
SESSION_DONE = 3
CRASHED = 3


def irsdk():
    return app.config['IR']


def field_size():
    pace_car_id = irsdk()['DriverInfo']['PaceCarIdx']
    return int(pace_car_id)


def car_id():
    return irsdk()['DriverInfo']['DriverCarIdx']


def car_position():  # 1 indexed
    positions = irsdk()['SessionInfo']['Sessions'][1]['ResultsPositions']
    driver_info = list(filter(lambda p: p['CarIdx'] == car_id(), positions))[0]
    return driver_info['Position']


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
    return irsdk()['SessionInfo']['Sessions'][1]['SessionLaps'] == 'unlimited'


def total_race_laps():
    return irsdk()['SessionInfo']['Sessions'][1]['SessionLaps']


def total_race_time():
    seconds_string = irsdk()['SessionInfo']['Sessions'][1]['SessionTime'][:-4]
    return float(seconds_string)



import irsdk
ir = irsdk.IRSDK()
ir.startup(test_file='test_races\\another_after_green.bin')