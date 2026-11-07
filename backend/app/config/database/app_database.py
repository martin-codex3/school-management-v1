from app.config.settings.app_settings import AppSettings
from sqlalchemy.ext.asyncio.session import AsyncSession, async_sessionmaker
from sqlalchemy.ext.asyncio.engine import create_async_engine
from sqlalchemy import MetaData


# this will establish the connection
class Base(MetaData):
    pass


# we will create the database engine here
app_database_engine = create_async_engine(
    url=AppSettings.public_database_url, echo=True
)

# we will create the session for the database here
Session = async_sessionmaker(
    class_=AsyncSession, bind=app_database_engine, expire_on_commit=False
)


async def app_session():
    async with Session.begin() as session:
        await session.run_sync(Base.create_all)
