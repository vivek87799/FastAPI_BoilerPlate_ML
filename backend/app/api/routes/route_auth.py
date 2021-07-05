from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse
from typing import List, TypedDict

# from app.db.schemas import NewUser
from app.db import schemas
from app.services import service_auth



router = APIRouter()

@router.post("/sign_up")
async def sign_up(user: schemas.NewUser):
    try:
        val = service_auth.sign_up(user)
    except AssertionError as error:
        return JSONResponse(status_code=200, content=str(error))
    return val

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/sign_in")
@router.post("/sign_in")
async def sign_in(user: OAuth2PasswordRequestForm=Depends()):
    try:
        val = service_auth.sign_in(user)
    except HTTPException as error:
        return error
    return val

"""
@router.post("/token")
async def demo_login_check(form_data: OAuth2PasswordRequestForm=Depends()):
    username = form_data.username
    password = form_data.password
    print(username, password)
    # return {username: password}
"""

@router.get("/")
async def home(sign_in: str=Depends(oauth2_scheme)):
    return {"hello": sign_in}