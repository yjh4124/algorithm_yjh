
import sys

input = sys.stdin.readline


def getPowMatrix(a_matrix, n, b):
    if b == 1:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                matrix[i][j] = a_matrix[i][j] % 1000
        return matrix

    if b == 2:
        return getSquareMatrix(a_matrix, n)

    if b >= 3:
        if b % 2 == 0:
            return getSquareMatrix((getPowMatrix(a_matrix, n, b // 2)), n)
        else:
            return getMulMatrix((getPowMatrix(a_matrix, n, b - 1)), a_matrix, n)


def getSquareMatrix(matrix, n):
    squareMatrix = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                squareMatrix[i][j] += matrix[i][k] * matrix[k][j]
            squareMatrix[i][j] %= 1000

    return squareMatrix


def getMulMatrix(matrix, a_matrix, n):
    mulMatrix = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                mulMatrix[i][j] += matrix[i][k] % 1000 * a_matrix[k][j] % 1000
            mulMatrix[i][j] %= 1000

    return mulMatrix


n, b = map(int, input().split())

a_matrix = tuple((tuple(map(int, input().split()))) for _ in range(n))


resultMatrix = getPowMatrix(a_matrix, n, b)

for i in resultMatrix:
    print(*i)
