import uuid
from typing import Annotated

from pydantic import BaseModel, ConfigDict, EmailStr, Field
from pydantic_extra_types.phone_numbers import PhoneNumberValidator

from app.schemas.branches.branch_schema import BranchResponseSchema

MalawiPhone = Annotated[
    str, PhoneNumberValidator(default_region="MW", supported_regions=["MW"])
]


class TenantSchemaBase(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    school_name: str = Field(min_length=5, max_length=50)
    school_type: str = Field(min_length=3, max_length=50)
    school_email: EmailStr
    school_phone: MalawiPhone
    address: str = Field(min_length=5, max_length=100)
    city: str = Field(min_length=5, max_length=50)
    country: str = Field(min_length=5, max_length=100)


# for updating the tenant
class UpdateTenantSchema(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    school_name: str | None = Field(default=None, min_length=5, max_length=100)
    school_type: str | None = Field(default=None, min_length=5, max_length=100)
    school_email: EmailStr | None = Field(default=None, min_length=3, max_length=255)
    school_phone: MalawiPhone | None = Field(default=None, min_length=3, max_length=255)
    address: str | None = Field(default=None, min_length=3, max_length=255)
    city: str | None = Field(default=None, min_length=3, max_length=255)
    country: str | None = Field(default=None, min_length=3, max_length=255)
    website_url: str | None = Field(default=None, min_length=3, max_length=255)
    registration_number: str | None = Field(default=None, min_length=3, max_length=30)
    school_code: str | None = Field(default=None, min_length=3, max_length=100)
    description: str | None = Field(default=None, min_length=3, max_length=255)
    settings: dict | None = Field(default=None, min_length=3, max_length=100)
    display_name: str | None = Field(default=None, min_length=5, max_length=100)
    secondary_email: EmailStr | None = Field(default=None, nnullable=True)
    ownership_type: str | None = Field(default=None, min_length=5, max_length=255)
    official_contact_person: str | None = Field(
        default=None, min_length=5, max_length=100
    )
    contact_person_email: EmailStr | None = Field(default=None)
    contact_person_phone: MalawiPhone | None = Field(default=None)
    district: str | None = Field(default=None, min_length=2, max_length=255)
    region: str | None = Field(default=None, min_length=5, max_length=255)
    postal_code: str | None = Field(default=None, min_length=5, max_length=255)


class TenantResponseSchema(BaseModel):
    id: uuid.UUID
    school_name: str
    school_type: str
    school_email: str
    school_phone: str
    address: str
    city: str
    country: str
    website_url: str | None
    registration_number: str | None
    school_code: str | None
    description: str | None
    settings: dict | None
    display_name: str | None
    secondary_email: EmailStr | None
    ownership_type: str | None
    official_contact_person: str | None
    contact_person_email: EmailStr | None
    contact_person_phone: MalawiPhone | None
    district: str | None
    region: str | None
    postal_code: str | None


# the response schema for the tenant branches
class TenantBranchesResponseSchema(BaseModel):
    id: uuid.UUID
    school_name: str
    school_type: str
    school_email: str
    school_phone: str
    address: str
    city: str
    country: str
    website_url: str | None
    registration_number: str | None
    school_code: str | None
    description: str | None
    settings: dict | None
    display_name: str | None
    secondary_email: EmailStr | None
    ownership_type: str | None
    official_contact_person: str | None
    contact_person_email: EmailStr | None
    contact_person_phone: MalawiPhone | None
    district: str | None
    region: str | None
    postal_code: str | None
    branches: list[BranchResponseSchema]

    model_config = ConfigDict(arbitrary_types_allowed=True, from_attributes=True)
