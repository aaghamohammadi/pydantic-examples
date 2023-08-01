from pprint import pprint

from pydantic import BaseModel, constr, field_validator


class Person(BaseModel):
    first_name: constr(min_length=2, strict=True)
    last_name: constr(min_length=2, strict=True)

    @field_validator("first_name", "last_name")
    @classmethod
    def to_title(cls, value):
        if value.isnumeric():
            raise ValueError(f"{value} is not a proper name")
        return value.title()


p1 = Person(first_name="alireza", last_name="aghamohammadi")
pprint(p1)
