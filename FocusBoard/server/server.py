from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Query
from typing import List
import json
from core.storage import load_json, save_json
from server.routes import router
from server.chat_handler import create_message, message_to_dict

app = FastAPI(title="FocusBoard Chat Server")

app.include_router(router)

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: dict):
        message_json = json.dumps(message)
        for connection in self.active_connections:
            await connection.send_text(message_json)

manager = ConnectionManager()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket, user: str = Query(...)):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            # Assume data is JSON string with "text" field
            try:
                message_data = json.loads(data)
                text = message_data.get("text", "")
                if not text:
                    continue
                # Create message
                message = create_message(user, text)
                message_dict = message_to_dict(message)
                # Save to JSON
                try:
                    messages = load_json("data/messages.json")
                    if isinstance(messages, dict):
                        messages = []
                    messages.append(message_dict)
                    save_json("data/messages.json", messages)
                except json.JSONDecodeError:
                    # If error, start with new list
                    save_json("data/messages.json", [message_dict])
                # Broadcast to all clients
                await manager.broadcast(message_dict)
            except json.JSONDecodeError:
                # Invalid JSON, ignore
                continue
    except WebSocketDisconnect:
        manager.disconnect(websocket)
