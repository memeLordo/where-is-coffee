from loguru import logger
from sqlalchemy import select

from .database import Base, engine, session_factory
from .model import UserORM


class ORM:

    @staticmethod
    def create_tables():
        engine.echo = True
        # Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        engine.echo = False

    @staticmethod
    def insert_user(telegram_id, api_id, api_hash):
        with session_factory() as session:
            new_user = UserORM(
                telegram_id=telegram_id,
                api_id=api_id,
                api_hash=api_hash,
            )
            session.add(new_user)
            # flush отправляет запрос в базу данных
            session.flush()
            session.commit()

    @staticmethod
    def get_user(telegram_id: int):
        with session_factory() as session:
            return session.get(UserORM, telegram_id).scalars().all()

    @staticmethod
    def select_users():
        with session_factory() as session:
            query = select(UserORM)
            result = session.execute(query)
            users = result.scalars().all()
            logger.debug(f"{users=}")
            return users

    @staticmethod
    def update_user(telegram_id: int, **kwargs):
        with session_factory() as session:
            user = session.get(UserORM, telegram_id)
            """add parametr"""
            for parametr, value in kwargs.items():
                user.__setattr__(parametr, value)
            session.refresh(user)
            session.commit()
