import uuid
from datetime import UTC, datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey, String
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
    address_line_1: Mapped[str] = mapped_column(String(100))
    address_line_2: Mapped[str] = mapped_column(String(100))
    city: Mapped[str] = mapped_column(String(100))
    nationality: Mapped[str] = mapped_column(String(100))
    district: Mapped[str] = mapped_column(String(100))
    is_deleted: Mapped[bool] = mapped_column(default=False)
    is_main_branch: Mapped[bool] = mapped_column(default=True)
    created_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(UTC)
    )
    updated_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(UTC)
    )

    # for the relationships
    tenant_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("tenants.id"), primary_key=True
    )
    tenant: Mapped[Tenant] = relationship(back_populates="branches")
