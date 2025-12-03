from aiogram.types import Message
from aiogram import BaseMiddleware
from database.session import db_session
from database.models import User

class BanCheckMiddleware(BaseMiddleware):
    async def on_process_message(self, message: Message, data: dict):
        user_id = message.from_user.id
        with db_session() as session:
            user = session.query(User).filter(User.telegram_id == user_id).first()
            if user and user.status == "banned":
                await message.answer("Ваш аккаунт заблокирован. Пожалуйста, обратитесь в поддержку.")
                return
