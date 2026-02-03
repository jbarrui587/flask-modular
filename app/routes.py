from flask import Blueprint
import socket
import os

web_bp = Blueprint("web", __name__)

@web_bp.route("/")
def index():
    return "<h1>Aplicación Flask P12</h1>"

@web_bp.route("/info")
def info():
    hostname = socket.gethostname()
    port = os.environ.get("PORT", "8000")
    return f"Instancia: {hostname} - Puerto: {port}"
