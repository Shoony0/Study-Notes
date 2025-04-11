from fastapi import APIRouter
from Product import schemas 
from Product.database import get_db
from Product import models
from fastapi.params import Depends
from sqlalchemy.orm import Session
from passlib.context import CryptContext


router = APIRouter(
    tags=["Sellers"],
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post("/seller", response_model=schemas.DisplaySeller)
def create_seller(request: schemas.Seller, db: Session = Depends(get_db)):
    hashed_password = pwd_context.hash(request.password)
    new_seller = models.Seller(username=request.username, email=request.email, password=hashed_password)
    db.add(new_seller)
    db.commit()
    db.refresh(new_seller)
    return new_seller