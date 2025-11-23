from main import are_anagrams

def test_simple_anagrams():
    assert are_anagrams("listen", "silent") == True
    assert are_anagrams("triangle", "integral") == True
    assert are_anagrams("арка", "кара") == True
    assert are_anagrams("кот", "ток") == True

def test_simple_non_anagrams():
    assert are_anagrams("hello", "world") == False
    assert are_anagrams("python", "java") == False
    assert are_anagrams("кот", "собака") == False
    assert are_anagrams("дом", "ком") == False

def test_case_insensitivity():
    assert are_anagrams("Listen", "Silent") == True
    assert are_anagrams("Triangle", "Integral") == True
    assert are_anagrams("АРКА", "кара") == True
    assert are_anagrams("КоТ", "ТоК") == True

def test_with_spaces():
    assert are_anagrams("astronomer", "moon starer") == True
    assert are_anagrams("the eyes", "they see") == True
    assert are_anagrams("waitress", "a stew sir") == True

def test_different_length():
    assert are_anagrams("cat", "cats") == False
    assert are_anagrams("dog", "godess") == False
    assert are_anagrams("a", "aa") == False

def test_empty_strings():
    assert are_anagrams("", "") == True
    assert are_anagrams(" ", " ") == True
    assert are_anagrams("", "a") == False

def test_single_character():
    assert are_anagrams("a", "a") == True
    assert are_anagrams("a", "A") == True
    assert are_anagrams("a", "b") == False

def test_same_word():
    assert are_anagrams("hello", "hello") == True
    assert are_anagrams("test", "test") == True
    assert are_anagrams("слово", "слово") == True

def test_numbers_in_words():
    assert are_anagrams("a1b2", "1a2b") == True
    assert are_anagrams("123", "321") == True
    assert are_anagrams("123", "1234") == False

def test_special_characters():
    assert are_anagrams("a-b", "b-a") == True
    assert are_anagrams("a.b", "b.a") == True
    assert are_anagrams("a!b", "b!a") == True

def test_long_anagrams():
    """Тест длинных анаграмм"""
    long_word1 = "a" * 100 + "b" * 50 + "c" * 25
    long_word2 = "b" * 50 + "c" * 25 + "a" * 100
    assert are_anagrams(long_word1, long_word2) == True
    
    long_word3 = long_word1 + "d"
    assert are_anagrams(long_word1, long_word3) == False
