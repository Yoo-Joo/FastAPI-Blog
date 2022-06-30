from fastapi import Depends, status, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, models, db, hashing

def getUser(id: int, db: Session = Depends(db.get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = f'User with the id of {id} is not available'
        )
    return user


def addUser(user: schemas.User, db: Session = Depends(db.get_db)):
    newUser = models.User(name = user.name, email = user.email, password = hashing.Hash.bcrypt(user.password))
    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    return newUser