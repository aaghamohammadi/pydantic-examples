from pprint import pprint

from pydantic import BaseModel, ConfigDict, Field


class Student(BaseModel):
    model_config = ConfigDict(populate_by_name=True, extra="ignore")

    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")
    stno: int = Field(alias="studentNumber")


data_dict = {
    "first_name": "Alireza",
    "last_name": "Aghamohammadi",
    "stno": 97301797,
    "gpa": 19.8,
}

data_json = """
{
    "firstName": "Alireza",
    "lastName": "Aghamohammadi",
    "studentNumber": 97301797,
    "gpa": 19.8
}
"""

s1 = Student.model_validate(data_dict)
pprint(s1)
pprint(s1.first_name)

s2 = Student.model_validate_json(data_json)
pprint(s2)
pprint(s2.stno)
