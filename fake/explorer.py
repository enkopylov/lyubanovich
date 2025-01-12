from typing import List

from model.explorer import Explorer

# фиктивные данные, которые позже утащим в БД
_explorers = [
    Explorer(
        name='Claude Hand',
        country='FR',
        description='Scare during full moons'
    ),
    Explorer(
        name='Noah Weiser',
        country='BY',
        description='Myopic machete man'
    ),
]


def get_all() -> List[Explorer]:
    """Возвращает исследователей"""
    return _explorers


def get_one(name: str) -> Explorer | None:
    for _explorer in _explorers:
        if _explorer.name == name:
            return _explorer
    return None


def create(explorer: Explorer) -> Explorer:
    """Добавление исследователя"""
    return explorer


def modify(explorer: Explorer) -> Explorer:
    """Частичное изменение исследователя"""
    return explorer


def replace(explorer: Explorer) -> Explorer:
    """Полная замена исследователя"""
    return explorer


def delete(name: str) -> bool:
    """Удаление записи о исследователе"""
    return None
