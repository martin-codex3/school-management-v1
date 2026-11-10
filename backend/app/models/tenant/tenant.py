import uuid

from sqlalchemy import JSON, String
from sqlalchemy.orm import Mapped, mapped_column, relationship


from app.utils.base import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.tenant_user.tenant_user import TenantUser


class Tenant(Base):
    __tablename__ = "tenants"
    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True, default=lambda: uuid.uuid4()
    )
    school_name: Mapped[str] = mapped_column(String(255), unique=True)
    school_type: Mapped[str] = mapped_column(String(255), index=True)
    school_email: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    school_phone: Mapped[str] = mapped_column(String(30))
    address: Mapped[str] = mapped_column(String(255), index=True)
    city: Mapped[str] = mapped_column(String(255))
    country: Mapped[str] = mapped_column(String(100))
    website_url: Mapped[str | None] = mapped_column(String(255), nullable=True)
    registration_number: Mapped[str | None] = mapped_column(String(30), nullable=True)
    school_code: Mapped[str | None] = mapped_column(String(50), nullable=True)
    description: Mapped[str | None] = mapped_column(String(255), nullable=True)
    settings: Mapped[dict[str, any]] = mapped_column(JSON, default={}, nullable=True)
    is_deleted: Mapped[bool | None] = mapped_column(default=False)

    application_users: Mapped[list["TenantUser"]] = relationship(
        back_populates="tenant", lazy="selectin"
    )
