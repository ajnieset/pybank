from fastapi import APIRouter


router = APIRouter(prefix="/accounts")

@router.get("/")
def get_account():
    ...