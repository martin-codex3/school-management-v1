import uuid
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.utils.base import Base

if TYPE_CHECKING:
    from app.models.roles.role import Role
    from app.models.tenant_user.tenant_user import TenantUser


class UserRole(Base):
    __tablename__ = "user_roles"

    tenant_user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("tenant_users.id"), primary_key=True
    )
    role_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("roles.id"), primary_key=True)

    tenant_user: Mapped[TenantUser] = relationship(back_populates="roles")
    role: Mapped[Role] = relationship(back_populates="tenant_users")
