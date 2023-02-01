#!/usr/bin/python3
"""Student to JSON with filter"""


class Student:
    """class Student that defines a student"""

    def __init__(self, first_name, last_name, age):
        """Instantiation of firs name, second name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student"""

        if attrs is not None:
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        else:
            return self.__dict__
