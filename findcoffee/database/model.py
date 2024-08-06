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
