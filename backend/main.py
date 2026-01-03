from fastapi import FastAPI
from routers import auth, live, arbitrage, predictions, payments, admin
from services.websocket import router as ws_router

app = FastAPI(
    title="ProScore AI",
    description="AI-driven sports intelligence platform",
    version="1.0.0"
)

app.include_router(auth.router, prefix="/auth")
app.include_router(live.router, prefix="/live")
app.include_router(arbitrage.router, prefix="/arbitrage")
app.include_router(predictions.router, prefix="/predictions")
app.include_router(payments.router, prefix="/payments")
app.include_router(admin.router, prefix="/admin")
app.include_router(ws_router)
