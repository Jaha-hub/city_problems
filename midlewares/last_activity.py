from aiogram.types import Message
from aiogram import BaseMiddleware
from datetime import datetime
from database.session import db_session
from database.models import User  # предполагаем, что есть модель User

class UserActivityMiddleware(BaseMiddleware):
    async def on_process_message(self, message: Message, data: dict):
        user_id = message.from_user.id
        with db_session() as session:
            user = session.query(User).filter(User.telegram_id == user_id).first()
            if user:
                user.last_activity = datetime.utcnow()  # Обновляем дату последней активности
                session.commit()
