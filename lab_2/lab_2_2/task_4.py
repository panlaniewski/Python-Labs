print("Введите размеры матрицы:")
rows, cols = int(input("Количество строк: ")), int(input("Количество столбцов: "))

matrix = []
for i in range(rows):
    row = input().split(" ")
    if len(row) == rows:
        matrix.append([int(x) for x in row])
        raise IndexError("Несоответствие размеров строки")
    elif len(row) < rows:
        print(f"Недостаточно элементов в строке! Должно быть {rows}")
    else:
        print(f"Слишком много элементов в строке! Должно быть {rows}")
    
print("Исходная матрица:")
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], end=" ")
    print()
    
def transpose(matrix: list):
    n, m = len(matrix), len(matrix[0])
    transpose = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(m):
            transpose[j][i] = matrix[i][j]
    return transpose

matrix = transpose(matrix)

print("Транспонированная матрица:")
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], end=" ")
    print()