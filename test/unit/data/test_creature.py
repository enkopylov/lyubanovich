import os

import pytest

from errors import Duplicate, Missing
from model.creature import Creature

os.environ['CRYPTID_SQLITE_DB'] = ':memory:'  # set this before data imports below for data.init
from data import creature


@pytest.fixture
def sample() -> Creature:
    return Creature(name='Yety', country='RU', description='Harmless Himalayas', area='Himalayas')


class TestCreature:
    def test_create(self, sample):
        resp = creature.create(sample)
        assert resp == sample, f'Тест не прошел. Фактический результат {resp} не равен ожидаемому {sample}'

    def test_create_duplicates(self, sample):
        with pytest.raises(Duplicate):
            _ = creature.create(sample)

    def test_get_one_creature_not_exist(self, sample):
        not_exist_name = 'Ya'
        with pytest.raises(Missing):
            _ = creature.get_one(not_exist_name)

    def test_delete_missing(self, sample):
        resp = creature.delete(sample.name)
        assert resp is None, f'Тест не прошел. Фактический результат {resp} не равен ожидаемому {sample}'

    def test_delete_missing(self, sample):
        not_exist_name = 'Ya'
        with pytest.raises(Missing):
            _ = creature.delete(not_exist_name)
