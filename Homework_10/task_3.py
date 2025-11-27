# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division

@pytest.mark.parametrize(
    'args, result',
    [
        pytest.param((10, 2), 5, marks=pytest.mark.smoke),
        ((100, -50), -2),
        pytest.param((39, 1), 39, marks=pytest.mark.skip(reason="ссылка на ошибку которую вынесли")),
        ((1000, 10, 5), 20),
        ((7, 0), None),
    ])
def test_all_division(args, result):
    if result is None:
        with pytest.raises(ZeroDivisionError):
            all_division(*args)
    else:
        assert all_division(*args) == result