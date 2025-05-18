# TypedDict example
from typing import TypedDict


class Student(TypedDict):
    name: str
    age: int


student: Student = {
    "name": "Marcy",
    "age": 25,
}

from typing import Optional  # noqa : F841

student["age"]  # This student now has autocompletion when accessing keys

# This also allows you to create typed dictionaries as you would a class
other_student = Student(name="Jared", age=23)

# This line now prints like a dictionary would:
print(other_student)
#  {'name': 'Jared', 'age': 23}
