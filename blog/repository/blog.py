from fastapi import Depends, status, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, models, db

def getBlogs(db: Session = Depends(db.get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


def getBlog(id: int, db: Session = Depends(db.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = f'Blog with the id of {id} is not available'
        )
    return blog


def addBlog(blog: schemas.Blog, db: Session = Depends(db.get_db)):
    newBlog = models.Blog(title = blog.title, body = blog.body, user_id = 1)
    db.add(newBlog)
    db.commit()
    db.refresh(newBlog)
    return newBlog


def putBlog(id: int, blog: schemas.Blog, db: Session = Depends(db.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = f'Blog with the id of {id} is not available'
        )
    blog.update({'title' : blog.title, 'body' : blog.body})
    db.commit()
    return {'detail' : f'Blog with the id of {id} is updated'}


def deleteBlog(id: int, db: Session = Depends(db.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = f'Blog with the id of {id} is not available'
        )
    blog.delete(synchronize_session = False)
    db.commit()
    return {'detail' : f'Blog with the id of {id} is deleted'}