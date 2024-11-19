from flask import Blueprint, jsonify
from app.db import get_db
from pymongo.errors import ServerSelectionTimeoutError

db_check_bp = Blueprint('db_check', __name__)

@db_check_bp.route('/health/db', methods=['GET'])
def check_db():
    try:
        # Test DB connection by listing collections
        get_db().list_collection_names()
        return jsonify({"status": "success", "message": "Database is connected"}), 200
    except ServerSelectionTimeoutError:
        return jsonify({"status": "error", "message": "Failed to connect to MongoDB"}), 500
