from datetime import datetime
from core.models import Message


def message_to_dict(message: Message) -> dict:
    """Convert a Message model to a dictionary for JSON storage."""
    return {
        "user": message.user,
        "text": message.text,
        "timestamp": message.timestamp.isoformat()
    }


def create_message(user: str, text: str) -> Message:
    """Create a new Message instance."""
    return Message(user=user, text=text, timestamp=datetime.now())
