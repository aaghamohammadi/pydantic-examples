from datetime import date
from pprint import pprint

from pydantic import BaseModel


class Job(BaseModel):
    title: str
    salary: int


class Person(BaseModel):
    name: str
    job: Job
    birth_date: date


p1 = Person(
    name="Alireza",
    job=Job(title="Software Engineering", salary=100_000),
    birth_date="1993-12-10",
)

pprint(p1)
