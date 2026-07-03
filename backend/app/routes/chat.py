from flask import Blueprint, request, jsonify

from extensions import db
from app.models.message import Message

chat_bp = Blueprint("chat", __name__)


@chat_bp.route("/chat", methods=["POST"])
def send_message():

    data = request.get_json()

    message = Message(

        sender_id=data["sender_id"],
        receiver_id=data["receiver_id"],
        message=data["message"]

    )

    db.session.add(message)
    db.session.commit()

    return jsonify({

        "message": "Message Sent"

    }), 201


@chat_bp.route("/chat", methods=["GET"])
def get_messages():

    messages = Message.query.all()

    result = []

    for msg in messages:

        result.append({

            "id": msg.id,
            "sender_id": msg.sender_id,
            "receiver_id": msg.receiver_id,
            "message": msg.message,
            "created_at": str(msg.created_at)

        })

    return jsonify(result), 200