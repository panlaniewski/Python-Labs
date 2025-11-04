word_1= list(input("Введите первое слово: ").lower())
word_2 = list(input("Введите второе слово: ").lower())

word_1.sort()
word_2.sort()

print("Слова являются анаграммами:", word_1 == word_2)