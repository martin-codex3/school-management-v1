from sqlalchemy import Column, ForeignKey, Table

from app.utils.base import Base

user_roles = Table(
    "user_roles",
    Base.metadata,
    Column("tenant_user_id", ForeignKey("tenant_users.id"), primary_key=True),
    Column("role_id", ForeignKey("roles.id"), primary_key=True),
)
