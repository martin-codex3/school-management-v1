from sqlalchemy import Column, ForeignKey, Table

from app.utils.base import Base

user_roles = Table(
    Base.metadata,
    tenant_user_id=Column(ForeignKey("tenant_users.id"), primary_key=True),
    role_id=Column(ForeignKey("roles.id"), primary_key=True),
)
