from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..db import get_db


router = APIRouter(prefix="/users")

@router.get("/")
def get_users(db: Session = Depends(get_db)):
    ...