word_1, word_2 = list(input("Введите первое слово: ")), list(input("Введите второе слово: "))

word_1.sort()
word_2.sort()

print("Слова являются анаграммами:", word_1 == word_2)