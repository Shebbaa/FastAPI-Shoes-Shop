from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..database import get_db
from ..services.auth_service import AuthService
from ..schemas.user import UserCreate, UserLogin, TokenResponse, UserResponse
from ..dependencies.auth import get_current_user
from ..models.user import User

router = APIRouter(prefix="/api/auth", tags=["auth"])


@router.post("/register", response_model=TokenResponse, status_code=status.HTTP_201_CREATED)
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    """Регистрация нового пользователя. Возвращает JWT токен."""
    service = AuthService(db)
    return service.register(user_data)


@router.post("/login", response_model=TokenResponse, status_code=status.HTTP_200_OK)
def login(credentials: UserLogin, db: Session = Depends(get_db)):
    """Вход в систему. Возвращает JWT токен."""
    service = AuthService(db)
    return service.login(credentials.email, credentials.password)


@router.get("/me", response_model=UserResponse, status_code=status.HTTP_200_OK)
def get_me(current_user: User = Depends(get_current_user)):
    """Получить данные текущего авторизованного пользователя."""
    return current_user
