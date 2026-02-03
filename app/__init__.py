from flask import Flask
import logging
import os
from app.api.endpoints import api_bp
from app.routes import web_bp

def create_app():
    app = Flask(__name__)

    # Ruta absoluta para logs
    log_dir = "/app/logs"
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, "app.log")

    # Configuración de logging explícita
    handler = logging.FileHandler(log_file)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    handler.setLevel(logging.INFO)

    # Añadir el handler al logger de Flask
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.INFO)

    # Registrar Blueprints
    app.register_blueprint(api_bp, url_prefix="/api")
    app.register_blueprint(web_bp)

    # Logging de cada request
    @app.before_request
    def log_request():
        app.logger.info("Petición HTTP recibida")

    return app
