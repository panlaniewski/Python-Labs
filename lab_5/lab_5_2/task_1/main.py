
def count_words(sentence):
    if not sentence or sentence.isspace():
        return 0
    else:
        return len(sentence.split())

