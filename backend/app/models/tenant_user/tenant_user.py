import uuid
from datetime import UTC, datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.user_roles.user_role import user_roles
from app.utils.base import Base

if TYPE_CHECKING:
    from app.models.application_user.application_user import ApplicationUser
    from app.models.roles.role import Role
    from app.models.tenant.tenant import Tenant


class TenantUser(Base):
    __tablename__ = "tenant_users"
    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True, default=lambda: uuid.uuid4()
    )
    application_user_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users.id"), primary_key=True
    )
    tenant_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("tenants.id"), primary_key=True
    )

    created_date: Mapped[datetime] = mapped_column(default=datetime.now(UTC))
    updated_date: Mapped[datetime] = mapped_column(default=datetime.now(UTC))
    application_user: Mapped[ApplicationUser] = relationship(back_populates="tenants")
    tenant: Mapped[Tenant] = relationship(back_populates="application_users")
    # for the roles here
    roles: Mapped[list[Role]] = relationship(
        back_populates="tenant_users", secondary=user_roles
    )
