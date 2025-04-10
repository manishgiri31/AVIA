import uuid
import bcrypt
from fastapi import Depends, HTTPException
from database import get_db
from models.user import User
from pydantic_schemas.user_create import UserCreate
from fastapi import APIRouter 
from sqlalchemy.orm import Session

from pydantic_schemas.user_login import UserLogin

router = APIRouter()


@router.post('/signup',status_code=201)
def signup_user(user: UserCreate,db:Session=Depends(get_db)):
    # extract the data thats coming from req
    print(user.name)
    print(user.email)
    print(user.password)
    # check if the user already exist in db
    user_db = db.query(User).filter(User.email == user.email).first()

    if  user_db:
        raise HTTPException(400,'User already exists!')
    
    hashed_pw = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())
    user_db = User(id=str(uuid.uuid4()), email=user.email, password=hashed_pw,name=user.name)

    # add the user to db
    db.add(user_db)
    db.commit()
    db.refresh(user_db)

    return user_db

@router.post('/login')
def login_user(user: UserLogin, db: Session = Depends(get_db)):
    #check if the user with the same email is exist or not
    user_db = db.query(User).filter(User.email==user.email).first()
    
    if not user_db:
        raise HTTPException(400,"User with this email doesn't exist!")
    
    #password is matched or not
    is_match=bcrypt.checkpw(user.password.encode(),user_db.password)

    if not is_match:
        raise HTTPException(400,'Incorrect Password!')
    
    return user_db

    pass 