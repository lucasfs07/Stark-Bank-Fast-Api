from fastapi import FastAPI, Request
from app.webhook_handler import handle_webhook
from app.scheduler import start_scheduler

app = FastAPI()

@app.on_event("startup")
def startup_event():
    start_scheduler()

@app.post("/webhook")
async def webhook(request: Request):
    return await handle_webhook(request)