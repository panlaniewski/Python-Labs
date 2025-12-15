from main import sum_by_fouth
import pytest
import random

@pytest.mark.parametrize("n, res", [
    (0, 0),
    (10, 12),
    (15, 24),
    (20, 40),
    (100, 1200),
])
def test_correct_sum(n, res):
    assert sum_by_fouth(n) == res

@pytest.mark.skip()    
def test_string_arg():
    with pytest.raises(ValueError):
        sum_by_fouth("10")

@pytest.mark.xfail()
def test_negative_arg():
    assert sum_by_fouth(-1) == 0
        
@pytest.fixture
def random_value():
    return round(random.random() * 100)

def test_random_value(random_value):
    assert sum_by_fouth(random_value) >= 0
    
def test_float_arg():
    with pytest.raises(ValueError):
        sum_by_fouth(10.5)