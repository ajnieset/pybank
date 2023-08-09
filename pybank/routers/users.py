from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from ..db import get_db
from ..models import User
from ..schemas import User as UserData, UserBase


router = APIRouter(prefix="/users")

@router.get("/{user_id}")
def get_users(user_id: int, db: Session = Depends(get_db)) -> UserData:
    return User.get_by_id(user_id, db)

@router.post("")
def create_user(data: UserBase, db: Session = Depends(get_db)):
    try:
        User.create_user(data, db)
    except Exception as e:
        print(e)
        return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response(status_code=status.HTTP_201_CREATED)
