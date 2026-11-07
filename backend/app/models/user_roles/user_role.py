from sqlalchemy import Column, ForeignKey, Table

from app.utils.base import Base

user_roles = Table(
    Base.metadata,
    Column("tenant_users", ForeignKey("tenant_users.id"), primary_key=True),
    Column("roles", ForeignKey("roles.id"), primary_key=True),
)
