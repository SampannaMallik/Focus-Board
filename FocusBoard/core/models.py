from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class User:
    username: str


@dataclass
class Message:
    user: str
    text: str
    timestamp: datetime


@dataclass
class Task:
    text: str
    done: bool = False
