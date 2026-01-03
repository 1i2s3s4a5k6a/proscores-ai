from fastapi import APIRouter, WebSocket
import asyncio

router = APIRouter()

@router.websocket("/ws/arbitrage")
async def arbitrage_stream(ws: WebSocket):
    await ws.accept()
    while True:
        await ws.send_json({
            "match": "Arsenal vs Chelsea",
            "roi": 4.6
        })
        await asyncio.sleep(5)
