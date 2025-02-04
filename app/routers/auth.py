from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import database, schemas, models, utils, oauth2

router = APIRouter(tags=['Authentication'])

@router.post('/login')
def login(
    user_credentials: OAuth2PasswordRequestForm = Depends(), 
    db: Session = Depends(database.get_db)
):
    # Authenticate user by email (username) and password
    user = db.query(models.User).filter(
        models.User.email == user_credentials.username
    ).first()

    # If user not found, raise an exception
    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="Invalid Credentials"
        )
    
    # Verify the provided password
    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="Invalid Credentials"
        )

    # Create an access token with the user's ID
    access_token = oauth2.create_access_token(data={"user_id": str(user.id)})  # Ensure user_id is a string

    # Return the access token and token type
    return {"access_token": access_token, "token_type": "bearer"}
