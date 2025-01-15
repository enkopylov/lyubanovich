import data.creature as data
from model.creature import Creature


def get_all() -> list[Creature]:
    return data.get_all()


def get_one(name: str) -> Creature | None:
    return data.get_one(name)


def create(creature: Creature) -> Creature:
    return data.create(creature)


def modify(creature: Creature) -> Creature:
    return data.modify(creature)


def replace(creature: Creature) -> Creature:
    return data.replace(creature)


def delete(creature: Creature) -> bool:
    return data.delete(creature)
