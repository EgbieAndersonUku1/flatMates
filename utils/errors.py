from dataclasses import dataclass


@dataclass
class NoHousmatesError(Exception):
    message: str