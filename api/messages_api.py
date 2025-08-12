from flask import Blueprint, request, jsonify
from uuid import uuid4

# Blueprint for API routes
messages_api = Blueprint('messages_api', __name__)

# In-memory message storage
messages = {}

# GET all messages
@messages_api.route('/api/messages', methods=['GET'])
def get_messages():
    return jsonify(list(messages.values())), 200

# GET a single message by ID
@messages_api.route('/api/messages/<msg_id>', methods=['GET'])
def get_message(msg_id):
    if msg_id not in messages:
        return jsonify({"error": "Message not found"}), 404
    return jsonify(messages[msg_id]), 200

# POST a new message
@messages_api.route('/api/messages', methods=['POST'])
def create_message():
    data = request.get_json()
    if not data or not data.get("name") or not data.get("email") or not data.get("message"):
        return jsonify({"error": "Invalid input"}), 400

    msg_id = str(uuid4())
    message = {
        "id": msg_id,
        "name": data["name"],
        "email": data["email"],
        "message": data["message"]
    }
    messages[msg_id] = message
    return jsonify(message), 201

# PUT (update) a message
@messages_api.route('/api/messages/<msg_id>', methods=['PUT'])
def update_message(msg_id):
    if msg_id not in messages:
        return jsonify({"error": "Message not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "No input"}), 400

    message = messages[msg_id]
    message.update({
        "name": data.get("name", message["name"]),
        "email": data.get("email", message["email"]),
        "message": data.get("message", message["message"])
    })
    return jsonify(message), 200

# DELETE a message
@messages_api.route('/api/messages/<msg_id>', methods=['DELETE'])
def delete_message(msg_id):
    if msg_id not in messages:
        return jsonify({"error": "Message not found"}), 404
    del messages[msg_id]
    return jsonify({"message": "Deleted"}), 200
