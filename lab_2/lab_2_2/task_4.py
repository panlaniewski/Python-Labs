print("Введите размеры матрицы:")
rows, cols = int(input("Количество строк: ")), int(input("Количество столбцов: "))

matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input()))
    matrix.append(row)
    
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