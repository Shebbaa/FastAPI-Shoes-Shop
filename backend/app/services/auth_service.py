from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi import HTTPException, status
import bcrypt

from ..repositories.user_repository import UserRepository
from ..schemas.user import UserCreate, UserResponse, TokenResponse, TokenData

SECRET_KEY = "your-super-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  


class AuthService:
    def __init__(self, db: Session):
        self.repo = UserRepository(db)

    def hash_password(self, password: str) -> str:
        return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

    def verify_password(self, plain: str, hashed: str) -> bool:
        return bcrypt.checkpw(plain.encode("utf-8"), hashed.encode("utf-8"))


    def create_access_token(self, user_id: int, email: str) -> str:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        payload = {"sub": str(user_id), "email": email, "exp": expire}
        return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

    def decode_token(self, token: str) -> TokenData:
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            user_id = int(payload.get("sub"))
            email = payload.get("email")
            return TokenData(user_id=user_id, email=email)
        except JWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Недействительный токен",
                headers={"WWW-Authenticate": "Bearer"},
            )

    def get_current_user(self, token: str) -> UserResponse:
        token_data = self.decode_token(token)
        user = self.repo.get_by_id(token_data.user_id)
        if not user or not user.is_active:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Пользователь не найден или деактивирован",
            )
        return user


    def register(self, data: UserCreate) -> TokenResponse:
        if self.repo.get_by_email(data.email):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Пользователь с таким email уже существует",
            )
        if self.repo.get_by_username(data.username):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Это имя пользователя уже занято",
            )

        hashed = self.hash_password(data.password)
        user = self.repo.create(
            email=data.email,
            username=data.username,
            hashed_password=hashed,
        )

        token = self.create_access_token(user.id, user.email)
        return TokenResponse(
            access_token=token,
            user=UserResponse.model_validate(user),
        )

    def login(self, email: str, password: str) -> TokenResponse:
        user = self.repo.get_by_email(email)
        if not user or not self.verify_password(password, user.hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Неверный email или пароль",
            )
        if not user.is_active:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Аккаунт деактивирован",
            )

        token = self.create_access_token(user.id, user.email)
        return TokenResponse(
            access_token=token,
            user=UserResponse.model_validate(user),
        )
