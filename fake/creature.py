from typing import List

from model.creature import Creature

# фиктивные данные, которые позже утащим в БД
_creatures = [
    Creature(
        name='Yeti',
        country='BY',
        area='Himalayas',
        description='Hirsute Himalayan'
    ),
    Creature(
        name='Bigfoot',
        country='RU',
        area='*',
        description='Sasquatch'
    ),
]


def get_all() -> List[Creature]:
    """Возвращает существ"""
    return _creatures


def get_one(name: str) -> Creature | None:
    for _creature in _creatures:
        if _creature.name == name:
            return _creature
    return None


def create(creature: Creature) -> Creature:
    """Добавление существа"""
    return creature


def modify(creature: Creature) -> Creature:
    """Частичное изменение существа"""
    return creature


def replace(creature: Creature) -> Creature:
    """Полная замена существа"""
    return creature


def delete(name: str) -> bool:
    """Удаление записи о существе"""
    return None
