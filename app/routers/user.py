from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas, utils
from ..database import get_db

router = APIRouter(
    prefix="/users",
    tags=['Users']
)

# /users/
# /users


##USER ROUTES:
#Create User:
@router.post("/", 
        status_code = status.HTTP_201_CREATED,
        response_model= schemas.UserOut)
def create_user(user:schemas.UserCreate,
    db: Session = Depends(get_db)):
    
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    
    new_user = models.User(
        email = user.email,
        password = user.password
        
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user 

@router.get("/{id}", response_model=schemas.UserOut)
def get_user(id: int,db: Session = Depends(get_db)):
    # cursor.execute(""" SELECT * FROM posts WHERE id= %s """,
    #             (str(id)))
    # post = cursor.fetchone()
    user = db.query(models.User).filter(models.User.id ==id).first()
    if not user: 
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,
                            detail = f"post with id : {id} not found" )
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'messsage': f"post with id : {id} not found" }
    return user
