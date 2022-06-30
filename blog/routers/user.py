from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from .. import schemas, db
from ..repository import user
from ..oauth2 import get_current_user


router = APIRouter(
    prefix = '/user',
    tags = ['Users']
)

@router.get('/get/{id}', response_model = schemas.ShowUser)
def getUser(id: int, db: Session = Depends(db.get_db), current_user: schemas.User = Depends(get_current_user)):
    return user.getUser(id, db)


@router.post('/add', response_model = schemas.ShowUser)
def addUser(user_req: schemas.User, db: Session = Depends(db.get_db), current_user: schemas.User = Depends(get_current_user)):
    return user.addUser(user_req, db)

