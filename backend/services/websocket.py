from fastapi import APIRouter, WebSocket
import asyncio

router = APIRouter()

# --- ADD THIS NEW SECTION BELOW ---
@router.post("/auth/login")
async def login(email: str):
    # This gives the frontend the "access_token" it is looking for
    return {"access_token": "dummy-token-for-now", "user": email}
# ----------------------------------

@router.websocket("/ws/arbitrage")
async def arbitrage_stream(ws: WebSocket):
    await ws.accept()
    while True:
        await ws.send_json({
            "match": "Arsenal vs Chelsea",
            "roi": 4.6
        })
        await asyncio.sleep(5)

