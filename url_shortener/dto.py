"""
dto stands for Data Transfer Object
"""
from typing import NamedTuple


class User(NamedTuple):
    email: str
