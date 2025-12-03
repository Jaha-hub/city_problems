from aiogram.types import Message
from aiogram import BaseMiddleware
from database.session import db_session
from database.models import User

class RoleCheckMiddleware(BaseMiddleware):
    async def on_process_message(self, message: Message, data: dict):
        user_id = message.from_user.id
        with db_session() as session:
            user = session.query(User).filter(User.telegram_id == user_id).first()
            if not user or user.status == "banned":
                await message.answer("Вы заблокированы или не зарегистрированы.")
                return

            if user.role not in data.get("allowed_roles", []):
                await message.answer("У вас нет доступа к этой функции.")
                return
