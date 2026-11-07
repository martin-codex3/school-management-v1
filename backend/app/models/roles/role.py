import uuid
from datetime import UTC, datetime
from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.user_roles.user_role import user_roles
from app.utils.base import Base

if TYPE_CHECKING:
    from app.models.tenant_user.tenant_user import TenantUser


class Role(Base):
    __tablename__ = "roles"
    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True, default=lambda: uuid.uuid4()
    )
    name: Mapped[str] = mapped_column(String(100), index=True, unique=True)
    description: Mapped[str] = mapped_column(String(255), index=True)
    created_date: Mapped[datetime] = mapped_column(default=datetime.now(UTC))
    updated_date: Mapped[datetime] = mapped_column(default=datetime.now(UTC))
    tenant_users: Mapped[list[TenantUser]] = relationship(
        back_populates="roles", secondary=user_roles, lazy="selectin"
    )
