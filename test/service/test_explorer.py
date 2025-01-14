from model.explorer import Explorer
from service import explorer as code

sample = Explorer(
    name='Claude Hand',
    country='FR',
    description='Scare during full moons'
)


class TestExplorer:
    def test_create(self):
        resp = code.create(sample)
        assert resp == sample, f'Тест не прошел. Фактический результат {resp} не равен ожидаемому {sample}'

    def test_get_exist_explorer(self):
        resp = code.get_one(name='Claude Hand')
        assert resp == sample, f'Тест не прошел. Фактический результат {resp} не равен ожидаемому {sample}'

    def test_get_not_exist_explorer(self):
        resp = code.get_one(name='Find')
        assert resp is None, f'Тест не прошел. В ответе ожидался None, но был получен {resp}'
