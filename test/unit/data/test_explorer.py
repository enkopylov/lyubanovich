import os

import pytest

from errors import Duplicate, Missing
from model.explorer import Explorer

os.environ['CRYPTID_SQLITE_DB'] = ':memory:'  # set this before data imports below for data.init
from data import explorer


@pytest.fixture
def sample() -> Explorer:
    return Explorer(name='Yety', country='RU', description='Harmless Himalayas', area='Himalayas')


class TestExplorer:
    def test_create(self, sample):
        resp = explorer.create(sample)
        assert resp == sample, f'Тест не прошел. Фактический результат {resp} не равен ожидаемому {sample}'

    def test_create_duplicates(self, sample):
        with pytest.raises(Duplicate):
            _ = explorer.create(sample)

    def test_get_one_creature_not_exist(self, sample):
        not_exist_name = 'Ya'
        with pytest.raises(Missing):
            _ = explorer.get_one(not_exist_name)

    def test_delete_missing(self, sample):
        resp = explorer.delete(sample.name)
        assert resp is None, f'Тест не прошел. Фактический результат {resp} не равен ожидаемому {sample}'

    def test_delete_missing(self, sample):
        not_exist_name = 'Ya'
        with pytest.raises(Missing):
            _ = explorer.delete(not_exist_name)
