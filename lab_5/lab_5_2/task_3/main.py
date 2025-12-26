
def is_palindrome(str):
    formatted_str = str.replace(" ", "").lower()
    return formatted_str == formatted_str[::-1]
        