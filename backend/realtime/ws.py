from fastapi import APIRouter, WebSocket, WebSocketDisconnect

router=APIRouter()

@router.websocket("/ws")
async def ws_endpoint(ws: WebSocket):
    await ws.accept()
    try:
        while True:
            data = await ws.receive_json()
            await ws.send_json(data)
    except WebSocketDisconnect:
        print("client disconnected")