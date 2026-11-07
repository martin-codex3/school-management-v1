from sqlalchemy.ext.asyncio.engine import create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from app.config.settings.app_settings import AppSettings


# this will establish the connection
class Base(DeclarativeBase):
    pass


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
    async with Session as session:
        yield session
