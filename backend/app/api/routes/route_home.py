from fastapi import APIRouter
from typing import List, TypedDict

router = APIRouter()

@router.get("/")
async def home_route() -> TypedDict:
    welcome_msg = {"message":"Home route for FastAPI Boilerplate"}
    return welcome_msg
