from typing import Annotated

from sqlalchemy.orm import Mapped, mapped_column

from .database import Base

primory_key = Annotated[int, mapped_column(primary_key=True)]


class UserORM(Base):
    __tablename__ = "Access Keys"

    id: Mapped[primory_key]
    telegram_id: Mapped[int]
    api_id: Mapped[int]
    api_hash: Mapped[str]

    def __init__(self, id, telegram_id, api_id, api_hash):
        self.id = id
        self.telegram_id = telegram_id
        self.api_id = api_id
        self.api_hash = api_hash
