from main import are_anagrams
import pytest

@pytest.mark.parametrize("w1, w2, expected", [
    ("listen", "silent", True),
    ("кот", "ток", True),
    ("hello", "world", False),
    ("дом", "ком", False),
    ("Listen", "Silent", True),
])
def test_basic_cases(w1, w2, expected):
    assert are_anagrams(w1, w2) is expected

@pytest.mark.parametrize("w1, w2", [
    ("astronomer", "moon starer"),
    ("the eyes", "they see"),
])
def test_with_spaces(w1, w2):
    assert are_anagrams(w1, w2) is True

@pytest.mark.parametrize("w1, w2, expected", [
    ("", "", True),
    (" ", " ", True),
    ("", "a", False),
    ("a", "A", True),
    ("a", "b", False),
])
def test_trivial_cases(w1, w2, expected):
    assert are_anagrams(w1, w2) is expected

@pytest.mark.parametrize("w1, w2, expected", [
    ("a1b2", "1a2b", True),
    ("123", "321", True),
    ("123", "1234", False),
])
def test_numbers_and_mixed(w1, w2, expected):
    assert are_anagrams(w1, w2) is expected

@pytest.mark.xfail(reason="Знаки препинания не фильтруются")
def test_punctuation_ignored():
    assert are_anagrams("a-b", "ab") is True

@pytest.mark.skip(reason="Unicode не поддерживается")
def test_unicode_normalization():
    assert are_anagrams("ёжа", "еяж") is True

