import uuid

from sqlalchemy.orm import Mapped, mapped_column
from utils.base import Base


class TenantUser(Base):
    __tablename__ = "tenant_users"
    id: Mapped[uuid.UUID] = mapped_column(
        primary_key=True, default=lambda: uuid.uuid4()
    )
