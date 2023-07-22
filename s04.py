from pprint import pprint

from pydantic import BaseModel, Field


class Student(BaseModel):
    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")
    stno: int = Field(alias="studentNumber")

    class Config:
        populate_by_name = True


data_dict = {
    "first_name": "Alireza",
    "last_name": "Aghamohammadi",
    "stno": 97301797,
}

data_json = """
{
    "firstName": "Alireza",
    "lastName": "Aghamohammadi",
    "studentNumber": 97301797
}
"""

s1 = Student.model_validate(data_dict)
pprint(s1)
pprint(s1.first_name)

s2 = Student.model_validate_json(data_json)
pprint(s2)
pprint(s2.stno)
