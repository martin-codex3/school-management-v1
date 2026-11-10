import uuid
from typing import Annotated

from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator
from pydantic_extra_types.phone_numbers import PhoneNumberValidator

MalawiPhone = Annotated[str, PhoneNumberValidator("MW", supported_regions=["MW"])]


class ApplicationUserSchemaBase(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    first_name: str = Field(min_length=3, max_length=20)
    last_name: str = Field(min_length=3, max_length=20)
    email: EmailStr
    phone_number: MalawiPhone
    password_hash: str = Field(min_length=10, max_length=20)

    # sample validations
    @field_validator("first_name")
    @classmethod
    def validate_first_name(cls, first_name: str):
        if first_name.isalnum():
            raise ValueError("Name cannot include numbers")
        return first_name

    @field_validator("last_name")
    @classmethod
    def validate_last_name(cls, last_name: str):
        if last_name.isalnum():
            raise ValueError("Name cannot include numbers")
        return last_name


# for updating the application user
class UpdateApplicationUserSchema(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    first_name: str | None = Field(default=None, min_length=3, max_length=20)
    last_name: str | None = Field(default=None, min_length=3, max_length=20)
    email: EmailStr | None = Field(default=None)
    phone_number: MalawiPhone | None = Field(default=None)
    bio: str | None = Field(default=None, min_length=5, max_length=100)
    profile_image_url: str | None = Field(default=None)
    password_hash: str | None = Field(default=None, min_length=10, max_length=20)

    # sample validations
    @field_validator("first_name")
    @classmethod
    def validate_first_name(cls, first_name: str):
        if first_name.isalnum():
            raise ValueError("Name cannot include numbers")
        return first_name

    @field_validator("last_name")
    @classmethod
    def validate_last_name(cls, last_name: str):
        if last_name.isalnum():
            raise ValueError("Name cannot include numbers")
        return last_name


class ApplicationUserResponse(BaseModel):
    id: uuid.UUID
    first_name: str
    last_name: str
    email: str
    phone_number: str
    bio: str | None
    profile_image_url: str | None
