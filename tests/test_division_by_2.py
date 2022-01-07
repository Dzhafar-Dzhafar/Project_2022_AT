import division_by_2
import pytest
@pytest.mark.parametrize("a, b, result", [(10, 2, 5),
                                          (20, 2, 10),
                                          (30, 2, 15),
                                          (5, 2, 2.5)])
def test_division_true(a, b, result):
    assert division_by_2.division(a, b) == result

#Проверку добавлю деление на '0' и ошибку типа данных

@pytest.mark.parametrize("expected, divider, division", [(ZeroDivisionError, 0, 10),
                                               (TypeError, "2", 20)])
def test_zero_division(expected, divider, division):
    with pytest.raises(ZeroDivisionError):
        division_by_2.division(division, divider)