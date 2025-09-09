# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest
import time
@pytest.mark.usefixtures('class_time_logger')
class TestMy:
    def test(self, test_time_logger):
        time.sleep(0.5)
        assert 10 / 5 == 2

    def test1(self, test_time_logger):
        time.sleep(1)
        assert 100 / 10 / -2 == -5

    def test2(self):
        time.sleep(1)
        assert 150 + 150 == 300