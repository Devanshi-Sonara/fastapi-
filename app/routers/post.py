from fastapi import  Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
# from typing import List,Optional 
# from sqlalchemy.sql.functions import func
from .. import models, schemas,oauth2
from ..database import get_db


router = APIRouter(
    prefix="/posts",
    tags=['Posts']
)

#hardcode some data for practice    
my_posts = [
    {
        "title": "post1",
        "content" : "content1",
        "id" : 1
    },
    {
        "title": "post2",
        "content" : "content2",
        "id" : 2
    }
]
#used with sql query
def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p["id"] == id:
            return i

@router.get("/")
def get_posts(db: Session = Depends(get_db)):
    # cursor.execute("""SELECT * FROM posts """)
    # posts = cursor.fetchall()
    posts = db.query(models.Post).all()
    return posts

#Create Post
@router.post("/", 
        status_code = status.HTTP_201_CREATED,
        response_model= schemas.PostRes)
def create(new_post : schemas.PostCreate,db: Session = Depends(get_db)
            ,  current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute(""" INSERT INTO posts (title, content, published) 
    #                VALUES (%s, %s, %s) RETURNING * """,
    #             (new_post.title,new_post.content,new_post.published))
    # post = cursor.fetchone()
    # conn.commit()
    
    # print(current_user.email)
    
    post = models.Post( owner_id = current_user.id,
        **new_post.dict()
    )
    db.add(post)
    db.commit()
    db.refresh(post)
    return post 

#Get One Post:
@router.get("/{id}")
def get_posts(id: int,db: Session = Depends(get_db)
                ,  current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute(""" SELECT * FROM posts WHERE id= %s """,
    #             (str(id)))
    # post = cursor.fetchone()

    post = db.query(models.Post).filter(models.Post.id ==id).first()
    if not post: 
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            details = f"post with id : {id} not found" )
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'messsage': f"post with id : {id} not found" }
    return post

#Delete One Post:
@router.delete("/{id}")
def delete_post(id:int,status_code = status.HTTP_204_NO_CONTENT,db: Session = Depends(get_db)
                ,  current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute(""" DELETE FROM posts WHERE id= %s returning * """,
    #             (str(id)))
    # delete_post = cursor.fetchone()
    # conn.commit()
    
    post_query = db.query(models.Post).filter(models.Post.id == id)

    post = post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action")

    post_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

#Update One Post:
@router.put("/{id}")
def update_post(id:int,new_post : schemas.PostCreate, db: Session = Depends(get_db)
                ,  current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute(""" UPDATE posts SET title = %s, content= %s, published= %s WHERE id= %s
    #                 RETURNING * """,
    #             (new_post.title,new_post.content,new_post.published, str(id)))
    # updated_post = cursor.fetchone()
    # conn.commit()
    
    post_query = db.query(models.Post).filter(models.Post.id ==id) 
    post = post_query.first()
    
    
    if post == None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail = "doesnt exist" )
    
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action")


    
    post_query.update(new_post.dict(), synchronize_session = False)
    db.commit()
    return post_query.first()