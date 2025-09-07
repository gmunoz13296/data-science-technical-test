from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/algorithm", tags=["algorithm"])

class Algorithm(BaseModel):
    number: int

@router.get("/{number}")
async def read_item(number: int):
    return {"number": number}
