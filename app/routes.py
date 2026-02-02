from flask import Blueprint, request
import socket

api_bp = Blueprint("api", __name__)

@api_bp.route("/info", methods=["GET"])
def info():
    container_name = socket.gethostname()
    port = request.host.split(":")[-1]

    return {
        "container": container_name,
        "port": port
    }
