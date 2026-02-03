from flask import Flask
import logging
import os
from app.api.endpoints import api_bp
from app.routes import web_bp


LOG_PATH = "/app/logs/app.log"
os.makedirs("/app/logs", exist_ok=True)

logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def create_app():
    app = Flask(__name__)

    os.makedirs("logs", exist_ok=True)

    logging.basicConfig(
        filename="logs/app.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    app.register_blueprint(api_bp, url_prefix="/api")
    app.register_blueprint(web_bp)

    @app.before_request
    def log_request():
        logging.info("Petición HTTP recibida")

    return app
