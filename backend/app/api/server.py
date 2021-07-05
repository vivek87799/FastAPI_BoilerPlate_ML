from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer

from app.api.routes import router as api_router
from app.db.database import ConnectionToDatabase

ConnectionToDatabase.get_conneciton()

title = "FastAPI Boilerplate"
description = "boilerplate for fastapi with login module and docker container" 
version = 0.1

oath2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_application() -> FastAPI():
    app = FastAPI(title=title, description=description, version=version)
    app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
    )
    app.include_router(api_router, prefix="/api")
    return app

app = get_application()
