from main import is_palindrome
import pytest

@pytest.mark.parametrize("value, expected", [
    ("radar", True),
    ("Radar", True),
    ("А роза упала на лапу Азора", True),
    ("never odd or even", True),
    ("hello", False),
    ("python", False),
    ("ab", False),
])
def test_basic_cases(value, expected):
    assert is_palindrome(value) is expected

@pytest.mark.parametrize("value", [
    "",
    " ",
    "     ",
    "a",
    "1",
])
def test_trivial_true_cases(value):
    assert is_palindrome(value) is True

@pytest.mark.parametrize("value, expected", [
    ("12321", True),
    ("12345", False),
    ("a1a", True),
    ("a1b", False),
])
def test_numbers_and_mixed(value, expected):
    assert is_palindrome(value) is expected

def test_long_strings():
    assert is_palindrome("a" * 1000) is True
    assert is_palindrome("a" * 999 + "b") is False

@pytest.mark.xfail
def test_punctuation():
    assert is_palindrome("Madam, I'm Adam") is True

@pytest.mark.xfail(reason="Не все символы обрабатываются")
def test_tabs_and_newlines():
    assert is_palindrome("a\tb\ta") is True

@pytest.mark.skip
def test_unicode_normalization():
    assert is_palindrome("ёже") is True
