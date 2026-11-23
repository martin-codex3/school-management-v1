import uuid
from datetime import datetime
from typing import Annotated

from pydantic import BaseModel, ConfigDict, EmailStr, Field
from pydantic_extra_types.phone_numbers import PhoneNumberValidator

MalawiPhone = Annotated[
    str, PhoneNumberValidator(default_region="MW", supported_regions=["MW"])
]


class CreateBranchSchema(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    branch_name: str = Field(min_length=5, max_length=100)
    branch_email: EmailStr
    branch_phone: MalawiPhone
    alternative_phone: MalawiPhone
    address_line_1: str = Field(min_length=5, max_length=100)
    address_line_2: str = Field(min_length=5, max_length=100)
    city: str = Field(min_length=3, max_length=100)
    nationality: str = Field(min_length=5, max_length=100)
    district: str = Field(min_length=4, max_length=100)
    is_main_branch: bool = Field(default=False)


class UpdateBranchSchema(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    branch_name: str | None = Field(default=None, min_length=5, max_length=100)
    branch_email: EmailStr | None = Field(default=None)
    branch_phone: MalawiPhone | None = Field(default=None)
    alternative_phone: MalawiPhone | None = Field(default=None)
    address_line_1: str | None = Field(default=None, min_length=5, max_length=100)
    address_line_2: str | None = Field(default=None, min_length=5, max_length=100)
    city: str | None = Field(default=None, min_length=3, max_length=100)
    nationality: str | None = Field(default=None, min_length=5, max_length=100)
    district: str | None = Field(default=None, min_length=4, max_length=100)
    is_main_branch: bool | None = Field(default=False)


class BranchResponseSchema(BaseModel):
    id: uuid.UUID
    branch_name: str
    branch_email: str
    branch_phone: str
    alternative_phone: MalawiPhone
    address_line_1: str
    address_line_2: str
    city: str
    nationality: str
    district: str
    is_main_branch: bool
    created_date: datetime
    updated_date: datetime
