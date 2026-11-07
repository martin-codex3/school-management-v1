from contextlib import asynccontextmanager

from fastapi import FastAPI


# the context manager
@asynccontextmanager
async def app_lifespan(app: FastAPI):
    print("hey mate we start here")
    yield
    print("This is the other context")


app = FastAPI(
    lifespan=app_lifespan,
    version="v1",
    title="School Management System",
    description="The full api documentation for the school management system.",
)


@app.get("")
def greeting():
    return {"message": "hey mate"}
