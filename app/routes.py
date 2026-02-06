from flask import Blueprint,jsonify
import logging
import os

web_bp = Blueprint("web", __name__)

@web_bp.route("/")
def index():
    logging.info('GET (info')
    return "<h1>Aplicación Flask P12</h1>"

@web_bp.route("/info")
def info():
    logging.info("GET /info")
    instance = os.getenv("HOSTNAME","unknown")
    port = os.getenv("PORT", "8000")
    return jsonify({"instance": instance, "port": port })
