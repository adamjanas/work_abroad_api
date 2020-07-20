from enum import Enum


class ChoiceEnum(Enum):
    @classmethod
    def choices(cls):
        return [(choice.value, choice.name) for choice in cls]


class Sex(ChoiceEnum):
    MALE = 1
    FEMALE = 2
