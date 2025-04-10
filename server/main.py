from fastapi import FastAPI
from models.base import Base
from routes import auth
from database import engine
import uuid
app =  FastAPI()

app.include_router(auth.router,prefix='/auth')

Base.metadata.create_all(engine)