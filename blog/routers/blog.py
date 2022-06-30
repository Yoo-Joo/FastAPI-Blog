from fastapi import APIRouter, Depends, status
from typing import List
from sqlalchemy.orm import Session

from .. import schemas, db
from ..oauth2 import get_current_user
from ..repository import blog

router = APIRouter(
    prefix = '/blog',
    tags = ['Blogs']
)

@router.get('/get', response_model = List[schemas.ShowBlog],)
def getBlogs(db: Session = Depends(db.get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.getBlogs(db)


@router.get('/get/{id}', status_code = status.HTTP_200_OK, response_model = schemas.ShowBlog)
def getBlog(id: int, db: Session = Depends(db.get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.getBlog(id, db)


@router.post('/add', status_code = status.HTTP_201_CREATED,)
def addBlog(blog_req: schemas.Blog, db: Session = Depends(db.get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.addBlog(blog_req, db)


@router.put('/put/{id}', status_code = status.HTTP_202_ACCEPTED,)
def putBlog(id: int, blog_req: schemas.Blog, db: Session = Depends(db.get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.putBlog(id, blog_req, db)


@router.delete('/delete/{id}', status_code = status.HTTP_204_NO_CONTENT,)
def deleteBlog(id: int, db: Session = Depends(db.get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.deleteBlog(id, db)