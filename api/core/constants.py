from enum import Enum


class ChoiceEnum(Enum):
    @classmethod
    def choices(cls):
        return [(choice.value, choice.name) for choice in cls]


class SEX(ChoiceEnum):
    M = 'MALE'
    F = 'FEMALE'
