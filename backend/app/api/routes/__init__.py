from fastapi import APIRouter, Depends, HTTPException
from app.api.routes.route_home import router as router_home
from app.api.routes.route_auth import router as router_auth

router = APIRouter()
router.include_router(router_home, prefix="/home", tags=['Home'])
router.include_router(router_auth, prefix="/auth", tags=["Authentication"])

"""
router = APIRouter(
    prefix="/items",
    tags=["items"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)
"""
