from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.config.database.app_database import app_database_engine, database_init


# the context manager
@asynccontextmanager
async def app_lifespan(app: FastAPI):
    await database_init()
    yield
    app_database_engine.dispose()


app = FastAPI(
    lifespan=app_lifespan,
    version="v1",
    title="School Management System",
    description="The full api documentation for the school management system.",
)


@app.get("")
def greeting():
    return {"message": "hey mate"}
