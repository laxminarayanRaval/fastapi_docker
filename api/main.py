from fastapi import FastAPI, HTTPException
from api.routers import addresses

app = FastAPI()

app.include_router(addresses.router, prefix="/api/addresses")