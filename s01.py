from pprint import pprint
from typing import List

from pydantic import BaseModel, ValidationError


class Student(BaseModel):
    stno: int
    courses: List[str]


s1 = Student(
    stno=97301797,
    courses=[
        "Software Development Methodologies",
        "Computer Performance Evaluation",
        "Formal Program Development",
        "Machine Learning Theory",
        "Patterns in Software Engineering",
    ],
)

pprint(s1.model_dump())

data = {
    "stno": "not an integer",
    "courses": [
        "Software Development Methodologies",
        "Computer Performance Evaluation",
        "Formal Program Development",
        "Machine Learning Theory",
        "Patterns in Software Engineering",
    ],
}

try:
    s2 = Student(**data)
except ValidationError as ex:
    pprint(ex.errors())
