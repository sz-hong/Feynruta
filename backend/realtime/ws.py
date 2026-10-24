from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from auth.tokens import get_user

router=APIRouter()

@router.websocket("/ws")
async def ws_endpoint(ws: WebSocket):
    await ws.accept()
    try:
        auth_msg = await ws.receive_json()
        
        username = auth_msg.get("username")
        token = auth_msg.get("token")
        actual_username = await get_user(token)
                    
        if actual_username is None or actual_username != username:
            await ws.send_json({
                "type": "ERROR",
                "message": "UNAUTHORIZED"
            })
            await ws.close(code=1008)
            return 
                    
        await ws.send_json({
            "type": "AUTH_OK",
            "username": actual_username
        })
        
        while True:
            msg = await ws.receive_json()
            
                
            await ws.send_json(msg)
    except WebSocketDisconnect:
        print("client disconnected")