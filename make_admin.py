from app.database import SessionLocal
from app.models.user import User

db = SessionLocal()
user = db.query(User).filter(User.email == 'admin@email.com').first()

if user:
    print('Нашёл пользователя:', user.username)
    user.is_admin = True
    db.commit()
    print('Готово! is_admin =', user.is_admin)
else:
    print('Пользователь не найден. Все юзеры:')
    all_users = db.query(User).all()
    for u in all_users:
        print(f'  id={u.id}, email={u.email}, username={u.username}')

db.close()