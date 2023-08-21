from fastapi import APIRouter, Depends, status
from fastapi.responses import Response
from sqlalchemy.orm import Session

from ..db import get_db
from ..models import Account
from ..schemas import AccountBase


router = APIRouter(prefix="/accounts")

@router.get("/{account_id}")
def get_account(account_id:int, db: Session = Depends(get_db)):
    return Account.get_by_id(account_id, db)

@router.post("")
def create_account(data: AccountBase, db: Session = Depends(get_db)):
    try:
        Account.create_account(data, db)
    except Exception as e:
        print(e)
        return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response(status_code=status.HTTP_201_CREATED)