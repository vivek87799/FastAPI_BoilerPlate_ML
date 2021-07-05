from fastapi import status, HTTPException
from app.models import model_user
from app.db.schemas import Token
from app.api.dependencies import create_access_token

from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(password, hash_password):
    return pwd_context.verify(password, hash_password)

def sign_up(user):
    
    try:
        new_user = model_user.User(username=user.username, password=get_password_hash(user.password))
        new_user.save()
        _users = model_user.User.objects()
        users = [{"username":user.username, "password":user.password} for user in _users]
        return users
    except Exception as error:
        assert False, error
    return {"message":"New user created" + get_password_hash(user.password)}

def sign_in(user_login):
    
    try:
        # Check if the user exists in the database else assert
        user = model_user.User.objects.get(username=user_login.username)
        if not verify_password(user_login.password, user.password):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Incorrect password')
        
        # access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(data={"sub": user.username})
        return {"access_token": access_token, "token_type": "bearer"}

    except HTTPException as error:
        return error
    except model_user.User.DoesNotExist as error:
        return  HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User does not exist')
    except Exception as error:
        assert False, error
    return {"message":"New user created" + get_password_hash(user.password)}
