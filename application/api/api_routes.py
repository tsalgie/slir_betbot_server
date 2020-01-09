#!python3
from flask import Blueprint, current_app as app
from .iracing_client\
    import *

api = Blueprint('api_bp', __name__,
                template_folder='templates',
                url_prefix='/api/v1')

@api.route('/multipliers/win', methods=['GET'])
def win_multiplier():
    irsdk()
    multiplier_floor = 1.15
    standings = self.iracing_client.standings()
    current_position = standings.index(app.config['IRACING_USER'])  # 0 indexed

    session_status = self.iracing_client.session_status()
    green_light = session_status['green']  # boolean

    multiplier = 10 + current_position

    # after green light, divide by 4
    if green_light:
        multiplier /= 4.0

    race_type = 'laps'  # or 'timed'
    if race_type == 'laps':
        half_race_laps = session_status['total_race_laps'] / 2
        decrease_mult_amount_each_lap = multiplier - multiplier_floor / half_race_laps
        multiplier -= (session_status['elapsed_laps'] * decrease_mult_amount_each_lap)
    else:
        half_race_time = session_status['total_race_time'] / 2  # in seconds
        decrease_mult_amount_each_second = multiplier - multiplier_floor / half_race_time
        multiplier -= (session_status['elapsed_seconds'] * decrease_mult_amount_each_second)

    return multiplier


@api.route('/multipliers/top5', methods=['GET'])
def top5_multiplier():
    multiplier_floor = 1.15
    standings = self.iracing_client.standings()
    current_position = standings.index(app.config['IRACING_USER'])  # 0 indexed

    session_status = self.iracing_client.session_status()
    green_light = session_status.json['green']  # boolean

    multiplier = 5 + ((current_position - 4) / 2)
    # value actually decreases throughout the race
    # after green light, divide by 3
    # how often does total get decreased? by how much?

    return multiplier


@api.route('/multipliers/finish', methods=['GET'])
def finish_multiplier():
    multiplier_floor = 1.15
    standings = self.iracing_client.standings()
    current_position = standings.index(app.config['IRACING_USER'])  # 0 indexed

    session_status = self.iracing_client.session_status()
    green_light = session_status.json['green']  # boolean

    field_size = 0  # http
    multiplier = 1.5  # between 1.5 and 2 depending on distance from med pos
    # value actually decreases throughout the race
    # after green light, divide by 2
    # how often does total get decreased? by how much?

    return multiplier


@api.route('/multipliers/crash', methods=['GET'])
def crash_multiplier():
    multiplier_floor = 1.15
    standings = self.iracing_client.standings()
    current_position = standings.index(app.config['IRACING_USER'])  # 0 indexed

    session_status = self.iracing_client.session_status()
    green_light = session_status.json['green']  # boolean

    field_size = 0  # http
    multiplier = 2  # between 2 and 4 depending on distance from med pos
    # value actually decreases throughout the race
    # after green light, divide by 2
    # how often does total get decreased? by how much?

    return multiplier
'''