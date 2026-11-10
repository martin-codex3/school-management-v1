from sqlalchemy.ext.asyncio.engine import create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession, async_sessionmaker

from app.config.settings.app_settings import AppSettings
from app.models.application_user.application_user import ApplicationUser  # noqa: F401
from app.models.roles.role import Role  # noqa: F401
from app.models.tenant.tenant import Tenant  # noqa: F401
from app.models.tenant_user.tenant_user import TenantUser  # noqa: F401
from app.models.user_roles.user_role import user_roles  # noqa: F401
from app.utils.base import Base

# we will create the database engine here
app_database_engine = create_async_engine(
    url=AppSettings.public_database_url, echo=True
)


# for opening the database connection here
async def database_init():
    async with app_database_engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)


# we will create the session for the database here
Session = async_sessionmaker(
    class_=AsyncSession, bind=app_database_engine, expire_on_commit=False
)


async def app_session():
    async with Session() as session:
        yield session
