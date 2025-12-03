from sqlalchemy.orm import Session
from database.models import User, Log
from datetime import datetime

def create_user(db: Session, telegram_id: str, full_name: str, phone: str, role: str):
    db_user = User(telegram_id=telegram_id, full_name=full_name, phone=phone, role=role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_telegram_id(db: Session, telegram_id: str):
    return db.query(User).filter(User.telegram_id == telegram_id).first()

def create_log(db: Session, user_id: int, action: str, details: str):
    db_log = Log(user_id=user_id, action=action, details=details)
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log
