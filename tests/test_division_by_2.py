import division_by_2
import pytest
@pytest.mark.parametrize("a, b, result", [(10, 2, 5),
                                          (20, 2, 10),
                                          (30, 2, 15),
                                          (5, 2, 2.5)])
def test_division_true(a, b, result):
    assert division_by_2.division(a, b) == result

