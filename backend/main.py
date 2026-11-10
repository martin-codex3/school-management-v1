from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi_faults import FaultRegistry

from app.config.database.app_database import app_database_engine, database_init
from app.routes.application_user.application_user_routes import appliication_user_router
from app.routes.auth.auth_router import auth_router


# the context manager
@asynccontextmanager
async def app_lifespan(app: FastAPI):
    await database_init()
    yield
    await app_database_engine.dispose()


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

app.include_router(router=appliication_user_router, prefix="/api/users", tags=["User"])

# for the cords here
allowed_origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"],
    allow_origins=[allowed_origins],
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
