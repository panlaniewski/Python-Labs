from main import count_words
import pytest 

@pytest.mark.parametrize("str, res", [
    ("Hello Python, hello pytest!", 4),
    ("Hello", 1),
    ("", 0),
    ("   ", 0),
    ("  \t  \n  ", 0),
    ("  Hello  it's  Python  ", 3),
    ("Hello, world! How are you?", 5),
    ("Hello\tWorld\ntest", 3),
    ("1 2 3 4 5", 5),
    ("2025 year", 2),
])
def test_sentence(str, res):
    assert count_words(str) == res

@pytest.mark.xfail
def test_wrong_arg_type():
    count_words(2)
    
@pytest.mark.skip
def test_none_input():
    assert count_words(None) == 0
    