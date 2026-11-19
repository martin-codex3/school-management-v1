import uuid
from typing import Annotated

from pydantic import BaseModel, ConfigDict, EmailStr, Field
from pydantic_extra_types.phone_numbers import PhoneNumberValidator

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
    school_email: EmailStr | None = Field(default=None, min_length=3, max_length=30)
    school_phone: MalawiPhone | None = Field(default=None, min_length=3, max_length=30)
    address: str | None = Field(default=None, min_length=3, max_length=30)
    city: str | None = Field(default=None, min_length=3, max_length=30)
    country: str | None = Field(default=None, min_length=3, max_length=30)
    website_url: str | None = Field(default=None, min_length=3, max_length=30)
    registration_number: str | None = Field(default=None, min_length=3, max_length=30)
    school_code: str | None = Field(default=None, min_length=3, max_length=30)
    description: str | None = Field(default=None, min_length=3, max_length=30)
    settings: dict | None = Field(default=None, min_length=3, max_length=30)


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
