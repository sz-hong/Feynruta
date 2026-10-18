import asyncio
import json
from websockets.asyncio.client import connect

async def main():
    async with connect("ws://127.0.0.1:8000/ws") as ws:
        await ws.send(json.dumps({"type": "PING", "req_id": 1, "payload": {}}))
        reply = await ws.recv()
        print("收到：", reply)

asyncio.run(main())