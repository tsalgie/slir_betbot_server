import unittest
import application
import json
from unittest.mock import patch
from application.api import api_routes
from application.api.iracing_client import GRID, LIGHTS_OUT, FINISHED, SESSION_DONE, CRASHED


def decrease_multiplier_helper(multiplier, multiplier_floor):
    multiplier += 2


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.app = application.create_app(config='config.DevConfig').test_client()

    @classmethod
    def tearDownClass(cls):
        cls.app = None

    @patch('application.api.iracing_client.car_position', return_value=3)
    @patch('application.api.iracing_client.session_status', return_value=GRID)
    @patch('application.api.api_routes.decrease_multiplier')
    def test_win_multiplier_grid(self, mock_car_position, mock_session_status, mock_decrease_multiplier):
        response_body = self.app.get('/api/v1/multipliers/win').data
        value = json.loads(response_body)['multiplier']

        self.assertEqual(value, 13)

    @patch('application.api.iracing_client.car_position', return_value=5)
    @patch('application.api.iracing_client.session_status', return_value=LIGHTS_OUT)
    @patch('application.api.api_routes.decrease_multiplier')
    def test_win_multiplier_lights_out(self, mock_car_position, mock_session_status, mock_decrease_multiplier):
        response_body = self.app.get('/api/v1/multipliers/win').data
        value = json.loads(response_body)['multiplier']

        self.assertEqual(value, 3.75)


if __name__ == '__main__':
    unittest.main()
