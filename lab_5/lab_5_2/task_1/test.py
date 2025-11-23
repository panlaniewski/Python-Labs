from main import count_words

def test_sentence():
    assert count_words("Hello Python, hello pytest!") == 4
    
def test_single_word():
    assert count_words("Hello") == 1

def test_empty_string():
    assert count_words("") == 0

def test_only_spaces():
    assert count_words("   ") == 0
    assert count_words("  \t  \n  ") == 0

def test_multiple_spaces():
    assert count_words("Hello    it's    Python") == 3
    assert count_words("  Hello  it's  Python  ") == 3

def test_with_punctuation():
    assert count_words("Hello, world! How are you?") == 5

def test_mixed_whitespace():
    assert count_words("Hello\tWorld\ntest") == 3

def test_numbers_as_words():
    assert count_words("1 2 3 4 5") == 5
    assert count_words("2024 year") == 2