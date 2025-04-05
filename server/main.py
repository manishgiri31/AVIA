from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app =  FastAPI()

DATABASE_URL='postgresql://postgres:1234@localhost:5432/aviamusicapp'

engine = create_engine(DATABASE_URL)
Sessionlocal = sessionmaker(autocommit = False,autoflush=False,bind=engine)

db = Sessionlocal()

class UserCreate(BaseModel):
    name: str
    email: str
    password: str
@app.post('/signup')
def signup_user(user: UserCreate):
    # extract the data thats coming from req
    print(user.name)
    print(user.email)
    print(user.password)
    # check if the user already exist in db
    # add the user to db
    pass
   