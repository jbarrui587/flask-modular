from flask import Blueprint, jsonify
import logging

from . import api_bp

@api_bp.route("/status")
def status():
    logging.info("GET /api/status")
    return jsonify({"status": "ok"})

@api_bp.route("/ping")
def ping():
    logging.info("GET /api/ping")
    return jsonify({"response": "pong"})

@api_bp.route("/items")
def items():
    logging.info("GET /api/items")
    return jsonify(["item1", "item2", "item3"])
