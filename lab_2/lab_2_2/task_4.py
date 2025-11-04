print("Введите размеры матрицы:")
rows, cols = int(input("Количество строк: ")), int(input("Количество столбцов: "))

matrix = []
print(f"Введите матрицу {rows} на {cols} построчно:")
for i in range(rows):
    row = input().split()
    matrix.append([int(x) for x in row[:cols]])

print("Исходная матрица:")
for i in range(rows):
    for j in range(cols):
        print(matrix[i][j], end=" ")
    print()

def transpose(matrix):
    n, m = len(matrix), len(matrix[0])
    transpose = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            transpose[j][i] = matrix[i][j]
    return transpose

transposed = transpose(matrix)

print("Транспонированная матрица:")
for i in range(len(transposed)):
    for j in range(len(transposed[0])):
        print(transposed[i][j], end=" ")
    print()