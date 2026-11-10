from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi_faults import Fault, FaultRegistry

from app.config.database.app_database import app_database_engine, database_init
from app.routes.auth.auth_router import auth_router


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

# we will mount the static files here
app.mount(
    "/static", app=StaticFiles(directory="static/uploads/profiles"), name="static"
)

app.include_router(
    router=auth_router, prefix="/api/authentication", tags=["Authentication"]
)

# for the fault registry here
api_faults = FaultRegistry(name="session-faults", faults=[])

faults = FaultRegistry.merge(
    api_faults, name="api", type_base="https://api.school-management/problems"
)

faults.install(
    app=app,
    include_http_exceptions=True,
    include_unhandled_error=True,
    include_validation_error=True,
)
