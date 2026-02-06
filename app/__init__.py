from flask import Flask
import logging
from app.api.endpoints import api_bp
from app.routes import web_bp

def create_app():
    app = Flask(__name__)

    logging.basicConfig(filename='logs/app.log', level=logging.INFO)

    app.register_blueprint(web_bp)
    app.register_blueprint(api_bp, url_prefix='/api')
    return app
