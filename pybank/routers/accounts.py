from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..db import get_db
from ..models import Account
from ..schemas import Account as AccountData


router = APIRouter(prefix="/accounts")

@router.get("/{account_id}")
def get_account(account_id:int, db: Session = Depends(get_db)):
    return Account.get_by_id(account_id, db)

@router.post("")
def create_account(db: Session = Depends(get_db)):
    data = AccountData(id=1, balance=0.00, user_id=1, User=None)
    Account.create_account(data, db)
    return "", 200