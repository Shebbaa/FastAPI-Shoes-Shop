from sqlalchemy.orm import Session
from ..models.user import User
from ..schemas.user import UserCreate

def get_user_by_name(db:Session, name:str):
    return db.query(User).filter(User.name == name).first()


def create_user(db: Session, user: UserCreate):
    db_user = User(
        name=user.name,
        hashed_password=user.password, 
        is_admin=False
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user