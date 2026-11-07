import uuid

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.utils.base import Base


class ApplicationUser(Base):
    __tablename__ = "users"
    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True, default=lambda: uuid.uuid4()
    )
    first_name: Mapped[str] = mapped_column(String(40))
    last_name: Mapped[str] = mapped_column(String(40))
    email: Mapped[str] = mapped_column(100)
    phone_number: Mapped[str] = mapped_column(String(20))
    password_hash: Mapped[str] = mapped_column(30)
