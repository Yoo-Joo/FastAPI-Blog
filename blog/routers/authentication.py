from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from blog import models

from .. import db, hashing, token

router = APIRouter(
    tags = ['Authentication']
)

@router.post('/login')
def login(login_req: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(db.get_db)):
    user = db.query(models.User).filter(models.User.email == login_req.username).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = f'User not found'
        )
    if not hashing.Hash.verify(user.password, login_req.password):
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = f'Incorrect password'
        )
    
    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}