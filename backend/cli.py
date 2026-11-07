import asyncio
from datetime import UTC, datetime

from sqlalchemy import func, select
from sqlalchemy.orm import lazyload
from typer import Typer

from app.config.database.app_database import Session
from app.models.roles.role import Role

app = Typer()

# the list of roles here
from typing import Any

available_roles: list[dict[str, Any]] = [
    # ==========================================
    # SCHOOL ADMINISTRATION
    # ==========================================
    {
        "name": "School Owner",
        "description": "Owns the school account and oversees school ownership, administration, and strategic settings.",
    },
    {
        "name": "School Administrator",
        "description": "Manages school operations, users, roles, permissions, school settings, and general administration.",
    },
    {
        "name": "Principal",
        "description": "Oversees the school's academic performance, staff, students, and overall operations.",
    },
    {
        "name": "Deputy Principal",
        "description": "Assists the principal in managing school operations, supervising staff, and overseeing academic activities.",
    },
    {
        "name": "Registrar",
        "description": "Manages student records, enrollment, transfers, academic registration, and student documentation.",
    },
    {
        "name": "Teacher",
        "description": "Manages assigned classes, teaches subjects, records attendance, creates assessments, and submits student marks.",
    },
    {
        "name": "Academic Coordinator",
        "description": "Coordinates curriculum delivery, academic schedules, teaching activities, and academic performance monitoring.",
    },
    {
        "name": "Accountant",
        "description": "Maintains financial records, processes transactions, reconciles accounts, and prepares financial reports.",
    },
    {
        "name": "Librarian",
        "description": "Manages library resources, book circulation, borrowing, returns, reservations, and library records.",
    },
    {
        "name": "Receptionist",
        "description": "Handles visitors, general enquiries, communication, and front-office administrative activities.",
    },
    {
        "name": "Parent / Guardian",
        "description": "Accesses linked children's profiles, attendance, academic results, invoices, payments, and school announcements.",
    },
    {
        "name": "Student",
        "description": "Accesses personal academic information, timetables, attendance, assignments, learning resources, and published results.",
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
