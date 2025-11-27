import pytest
import time


@pytest.fixture(scope='class')
def class_time_logger():
    start = time.time()
    print('Запуск класса')
    yield
    end = time.time()
    print(f'Завершение класса {end - start} секунд время выполнения')
@pytest.fixture
def test_time_logger():
    start = time.time()
    yield
    end = time.time()
    print(f'{end - start} секунд время выполнения теста')