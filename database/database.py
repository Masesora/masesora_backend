from motor.motor_asyncio import AsyncIOMotorClient
from typing import Any
import os

# -----------------------------------------
# CONFIGURACIÓN MONGO (CORREGIDA PARA RENDER)
# -----------------------------------------

# Render NO tiene MongoDB local → localhost NO funciona.
# Usamos variable de entorno para que puedas poner Atlas u otra URL.
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")

DB_NAME = "masesora"

client: AsyncIOMotorClient | None = None
db: Any = None


# -----------------------------------------
# CONEXIÓN
# -----------------------------------------

async def connect_to_mongo() -> None:
    global client, db
    client = AsyncIOMotorClient(MONGO_URI)
    db = client[DB_NAME]


async def close_mongo_connection() -> None:
    global client
    if client:
        client.close()


# -----------------------------------------
# UTILIDAD
# -----------------------------------------

def get_collection(name: str):
    return db[name]