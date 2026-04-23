import json
import os
from typing import Any, Dict, List


def load_json(file_path: str) -> Any:
    """Load data from a JSON file. Returns empty dict if file doesn't exist."""
    if not os.path.exists(file_path):
        return {}
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_json(file_path: str, data: Any) -> None:
    """Save data to a JSON file."""
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
