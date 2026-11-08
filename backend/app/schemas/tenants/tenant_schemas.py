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
