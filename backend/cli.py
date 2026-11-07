import asyncio
from datetime import UTC, datetime

from sqlalchemy import func, select
from sqlalchemy.orm import lazyload
from typer import Typer

from app.config.database.app_database import Session
from app.models.roles.role import Role

app = Typer()

# the list of roles here
available_roles: list[dict[str, any]] = [
    {
        "name": "Administrator",
        "description": "This is the main description for the role",
    },
    {
        "name": "Teacher",
        "description": "Responsible for managing classes and students",
    },
    {
        "name": "Student",
        "description": "Responsible for accessing learning resources",
    },
]


async def seed_roles():
    async with Session() as session:
        statement = await session.execute(select(Role))
        existing_roles = statement.scalars().all()

        for role in available_roles:
            if role not in existing_roles:
                return

        new_role = Role(
            **role, created_date=datetime.now(UTC), updated_date=datetime.now(UTC)
        )

        session.add(new_role)
        await session.commit()


@app.command()
def roles():
    asyncio.run(seed_roles())


if __name__ == "__main__":
    app()
