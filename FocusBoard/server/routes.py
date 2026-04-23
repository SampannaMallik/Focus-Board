from fastapi import APIRouter
from core.storage import load_json
import json

router = APIRouter()

@router.get("/messages")
def get_messages():
    """Return all saved messages."""
    try:
        data = load_json("data/messages.json")
        # If data is dict (empty), return empty list
        if isinstance(data, dict):
            return []
        return data
    except json.JSONDecodeError:
        # If file is empty or invalid, return empty list
        return []
