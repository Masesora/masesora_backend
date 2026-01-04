from fastapi import APIRouter, Request
from masesora_backend.database.database import get_collection
from datetime import datetime

router = APIRouter()

@router.post("/ese")
async def registrar_ese(request: Request):
    data = await request.json()
    data["timestamp"] = datetime.utcnow().isoformat()
    collection = get_collection("ese_registros")
    result = await collection.insert_one(data)
    return {"id": str(result.inserted_id), "status": "registrado"}