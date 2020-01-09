from flask import Blueprint, render_template

# Set up a Blueprint
charts = Blueprint('charts_bp', __name__,
                   template_folder='templates',
                   static_folder='static')


@charts.route('/leaderboard', methods=['GET'])
def leaderboard():
    """Points leaderboard"""
    return render_template('leaderboard.html')


@charts.route('/multipliers', methods=['GET'])
def multipliers():
    """Multipliers based on race distance"""
    return render_template('multipliers.html')
