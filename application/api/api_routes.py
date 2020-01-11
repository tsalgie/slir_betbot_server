#!python3
from flask import Blueprint, current_app as app
from .iracing_client\
    import *

api = Blueprint('api_bp', __name__,
                template_folder='templates',
                url_prefix='/api/v1')


def decrease_multiplier(multiplier, multiplier_floor):
    if timed_race():
        half_race_time = total_race_time() / 2  # in seconds
        decrease_mult_amount_each_second = (multiplier - multiplier_floor) / half_race_time
        multiplier -= elapsed_seconds() * decrease_mult_amount_each_second
    else:
        half_race_laps = total_race_laps() / 2
        decrease_mult_amount_each_lap = (multiplier - multiplier_floor) / half_race_laps
        multiplier -= elapsed_laps() * decrease_mult_amount_each_lap


@api.route('/multipliers/win', methods=['GET'])
def win_multiplier():
    multiplier_floor = 1.15
    current_position = car_position()

    multiplier = 10 + current_position

    # after lights out, divide by 4
    if session_status() == LIGHTS_OUT:
        multiplier /= 4.0

    # value decreases throughout the race
    decrease_multiplier(multiplier, multiplier_floor)

    return multiplier


@api.route('/multipliers/top5', methods=['GET'])
def top5_multiplier():
    multiplier_floor = 1.15
    current_position = car_position()

    multiplier = 5 + ((current_position - 4) / 2)

    # after green light, divide by 3
    if session_status() == LIGHTS_OUT:
        multiplier /= 3.0

    # value decreases throughout the race
    decrease_multiplier(multiplier, multiplier_floor)

    return multiplier


@api.route('/multipliers/finish', methods=['GET'])
def finish_multiplier():
    multiplier_floor = 1.15
    current_position = car_position()
    grid_size = field_size()

    multiplier = 1.5 + (abs(current_position-grid_size/2) / grid_size)  # between 1.5 and 2 depending on distance from med pos

    # after green light, divide by 2
    if session_status() == LIGHTS_OUT:
        multiplier /= 2.0

    # value decreases throughout the race
    decrease_multiplier(multiplier, multiplier_floor)

    return multiplier


@api.route('/multipliers/crash', methods=['GET'])
def crash_multiplier():
    multiplier_floor = 1.15
    current_position = car_position()
    grid_size = field_size()

    multiplier = 2 + (4 * abs(current_position-grid_size/2) / grid_size)  # between 2 and 4 depending on distance from med pos

    # after green light, divide by 2
    if session_status() == LIGHTS_OUT:
        multiplier /= 2.0

    # value decreases throughout the race
    decrease_multiplier(multiplier, multiplier_floor)

    return multiplier
