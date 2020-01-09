from flask import Flask, g
import irsdk


def create_app(config='config.ProdConfig'):
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(config)

    with app.app_context():
        # Import application components
        from .api import api_routes
        from .charts import charts_routes
        app.register_blueprint(api_routes.api)
        app.register_blueprint(charts_routes.charts)

        ir = irsdk.IRSDK()
        ir.startup(test_file='./before_green.bin')

        app.config['IR'] = ir

        return app
