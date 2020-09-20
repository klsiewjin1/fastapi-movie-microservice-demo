from fastapi import APIRouter, HTTPException

from . import db_manager
from .models import CastOut, CastIn

casts = APIRouter()


@casts.post("/", response_model=CastOut, status_code=201)
async def create_cast(payload: CastIn):
    cast_id = await db_manager.add_cast(payload)
    response = {"id": cast_id, **payload.dict()}

    return response


@casts.get("/{id}/", response_model=CastOut)
async def get_cast(id: int):
    cast = await db_manager.get_cast(id)
    if not cast:
        raise HTTPException(status_code=404, detail="Cast not found")
    return cast
