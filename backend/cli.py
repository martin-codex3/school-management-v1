import asyncio
from datetime import UTC, datetime

from sqlalchemy import func, select
from typer import Typer

from app.config.database.app_database import Session
from app.models.roles.role import Role

app = Typer()

# the list of roles here
available_roles: list[Role] = [
    {
        "name": "Administrator",
        "description": "This is the main description for the role",
        "created_date": datetime.now(UTC),
        "updated_date": datetime.now(UTC),
    }
]


async def seed_roles():
    async with Session() as session:
        statement = await session.execute(select(Role))
        roles = statement.scalars().all()
        print(roles)


@app.command()
def roles():
    asyncio.run(seed_roles())


if __name__ == "__main__":
    app()
