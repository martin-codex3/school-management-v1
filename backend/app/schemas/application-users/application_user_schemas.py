from typing import Annotated

from pydantic import BaseModel, ConfigDict, EmailStr, Field
from pydantic_extra_types.phone_numbers import PhoneNumberValidator

MalawiPhone = Annotated[str, PhoneNumberValidator("MW", number_format=["MW"])]


class ApplicationUserSchemaBase(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    first_name: str = Field(min_length=3, max_length=20)
    last_name: str = Field(min_length=3, max_length=20)
    email: EmailStr
    phone_number: MalawiPhone
    password_hash: str = Field(min_length=10, max_length=20)
