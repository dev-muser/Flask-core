from flask import Flask
from config import config

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    from .main import main as main_bluprint
    app.register_blueprint(main_bluprint)

    return app
