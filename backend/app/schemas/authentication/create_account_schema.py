from typing import Annotated

from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator
from pydantic_extra_types.phone_numbers import PhoneNumberValidator

MalawiPhone = Annotated[
    str, PhoneNumberValidator(default_region="MW", supported_regions=["MW"])
]


class CreateAccountSchema(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    first_name: str = Field(min_length=3, max_length=20)
    last_name: str = Field(min_length=3, max_length=20)
    email: EmailStr
    phone_number: MalawiPhone
    school_name: str = Field(min_length=5, max_length=50)
    school_type: str = Field(min_length=3, max_length=50)
    school_email: EmailStr
    school_phone: MalawiPhone
    address: str = Field(min_length=5, max_length=100)
    city: str = Field(min_length=5, max_length=50)
    country: str = Field(min_length=5, max_length=100)
    password_hash: str = Field(min_length=10, max_length=20)

    # sample validations
    @field_validator("first_name")
    @classmethod
    def validate_first_name(cls, first_name: str):
        if not first_name.isalpha():
            raise ValueError("Name cannot include numbers")
        return first_name

    @field_validator("last_name")
    @classmethod
    def validate_last_name(cls, last_name: str):
        if not last_name.isalpha():
            raise ValueError("Name cannot include numbers")
        return last_name
