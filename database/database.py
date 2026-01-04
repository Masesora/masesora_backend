from motor.motor_asyncio import AsyncIOMotorClient
from typing import Any

MONGO_URI = "mongodb://localhost:27017"
DB_NAME = "masesora"

client: AsyncIOMotorClient | None = None
db: Any = None

async def connect_to_mongo() -> None:
    global client, db
    client = AsyncIOMotorClient(MONGO_URI)
    db = client[DB_NAME]

async def close_mongo_connection() -> None:
    global client
    if client:
        client.close()
def get_collection(name: str):
    return db[name]