from model.creature import Creature
from service import creature as code

sample = Creature(
    name='Yeti',
    country='BY',
    area='Himalayas',
    description='Hirsute Himalayan'
)


class TestCreature:
    def test_create(self):
        resp = code.create(sample)
        assert resp == sample, f'Тест не прошел. Фактический результат {resp} не равен ожидаемому {sample}'

    def test_get_exist_creature(self):
        resp = code.get_one(name='Yeti')
        assert resp == sample, f'Тест не прошел. Фактический результат {resp} не равен ожидаемому {sample}'

    def test_get_not_exist_creature(self):
        resp = code.get_one(name='Find')
        assert resp is None, f'Тест не прошел. В ответе ожидался None, но был получен {resp}'
