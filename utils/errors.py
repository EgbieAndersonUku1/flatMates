from dataclasses import dataclass


@dataclass
class NoHousmatesError(Exception):
    message: str


@dataclass
class invalidMonthError(Exception):
    message: str

