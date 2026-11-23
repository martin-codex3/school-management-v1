import uuid
from datetime import UTC, datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.utils.base import Base

if TYPE_CHECKING:
    from app.models.tenant.tenant import Tenant


class Branch(Base):
    __tablename__ = "branches"

    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True, default=lambda: uuid.uuid4()
    )
    branch_name: Mapped[str] = mapped_column(String(255))
    branch_email: Mapped[str] = mapped_column(String(255), unique=True)
    branch_phone: Mapped[str] = mapped_column(String(100))
    alternative_phone: Mapped[str] = mapped_column(String(100))
