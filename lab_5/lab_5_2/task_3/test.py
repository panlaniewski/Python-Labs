from main import is_palindrome

def test_simple_palindromes():
    assert is_palindrome("radar") == True
    assert is_palindrome("level") == True

def test_simple_non_palindromes():
    assert is_palindrome("hello") == False
    assert is_palindrome("world") == False
    assert is_palindrome("python") == False

def test_case_insensitivity():
    assert is_palindrome("Radar") == True
    assert is_palindrome("Level") == True
    assert is_palindrome("А роза упала на лапу Азора") == True
    assert is_palindrome("Madam") == True

def test_with_spaces():
    assert is_palindrome("а роза упала на лапу азора") == True
    assert is_palindrome("was it a car or a cat i saw") == True
    assert is_palindrome("never odd or even") == True
    assert is_palindrome("топот") == True

def test_empty_string():
    assert is_palindrome("") == True 
    assert is_palindrome(" ") == True 

def test_single_character():
    assert is_palindrome("a") == True
    assert is_palindrome("я") == True
    assert is_palindrome("1") == True

def test_two_characters():
    assert is_palindrome("aa") == True
    assert is_palindrome("ab") == False
    assert is_palindrome("no") == False
    assert is_palindrome("oo") == True

def test_numbers():
    assert is_palindrome("12321") == True
    assert is_palindrome("12345") == False
    assert is_palindrome("1") == True
    assert is_palindrome("11") == True

def test_mixed_alphanumeric():
    assert is_palindrome("a1a") == True
    assert is_palindrome("a1b") == False
    assert is_palindrome("1a1") == True

def test_long_palindromes():
    long_palindrome = "a" * 1000
    assert is_palindrome(long_palindrome) == True
    
    long_non_palindrome = "a" * 999 + "b"
    assert is_palindrome(long_non_palindrome) == False