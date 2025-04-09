import asyncio
import httpx
from sqlalchemy.orm import Session
from app.models import SyncLog
from app.database import SessionLocal


def log_sync_attempt(status: str, message: str):
    db: Session = SessionLocal()
    log = SyncLog(status=status, message=message)
    db.add(log)
    db.commit()
    db.close()


async def check_network_and_sync():
    await asyncio.sleep(5)
    while True:
        try:
            # Check internet using blocking request (OK since it's quick)
            import requests
            requests.get("https://www.google.com", timeout=3)
            print(" Internet is available. Syncing...")

            # Use httpx for async-compatible request to FastAPI endpoint
            async with httpx.AsyncClient() as client:
                response = await client.post("http://127.0.0.1:8080/api/sync")

                if response.status_code == 200:
                    log_sync_attempt("success", "Synced successfully")
                else:
                    log_sync_attempt("failed", f"Sync failed: {response.text}")

        except Exception as e:
            print(" No internet connection. Will retry...")
            log_sync_attempt("failed", str(e))

        await asyncio.sleep(60)
