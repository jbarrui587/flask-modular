from flask import jsonify
from . import api_bp

@api_bp.route('/status')
def status():
    return jsonify({"status": "ok"})


@api_bp.route('/ping')
def ping():
    return jsonify({"response": "pong"})


@api_bp.route('/items')
def items():
    return jsonify(["item1", "item2", "item3"])
