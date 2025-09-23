text = input("Введите текст: ")

sep_chr = ",.:?!-()'"
text_lst = ''.join([char for char in text if char not in sep_chr]).lower().split()
words_dict = { word.strip(): text_lst.count(word) for word in text_lst if word != ""}
unique_words = 0

for key in words_dict:
    if words_dict[key] == 1:
       unique_words += 1 

print("Словарь слов текста:", words_dict)
print("Количество уникальных слов:", unique_words) 