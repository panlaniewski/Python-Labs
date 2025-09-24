text = input("Введите текст: ")

sep_chr = ",.:?!-()';"
text_lst = ''.join([char for char in text if char not in sep_chr]).lower().split()

words_dict = {}
for word in text_lst:
    words_dict[word] = words_dict.get(word, 0) + 1

print("Словарь слов текста:", words_dict)
print("Количество уникальных слов:", len(words_dict)) 