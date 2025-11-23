
def are_anagrams(word1, word2):
    cleaned_word1 = word1.replace(" ", "").lower()
    cleaned_word2 = word2.replace(" ", "").lower()
    return sorted(cleaned_word1) == sorted(cleaned_word2)