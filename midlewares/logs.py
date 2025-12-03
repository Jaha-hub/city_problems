from aiogram.types import Message, CallbackQuery
from aiogram import BaseMiddleware
from datetime import datetime
from database.session import db_session
from database.models import Log

class LoggingMiddleware(BaseMiddleware):
    async def on_process_message(self, message: Message, data: dict):
        with db_session() as session:
            log = Log(
                user_id=message.from_user.id,
                action="send_message",
                details=message.text,
                created_at=datetime.utcnow()
            )
            session.add(log)
            session.commit()

    async def on_process_callback_query(self, callback_query: CallbackQuery, data: dict):
        with db_session() as session:
            log = Log(
                user_id=callback_query.from_user.id,
                action="click_button",
                details=callback_query.data,
                created_at=datetime.utcnow()
            )
            session.add(log)
            session.commit()
