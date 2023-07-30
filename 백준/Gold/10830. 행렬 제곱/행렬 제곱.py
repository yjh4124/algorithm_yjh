import sys

a, b = map(int, input().split())
matrix=tuple(tuple(map(int, sys.stdin.readline().split())) for _ in range(a))

def getPowMatrix(matrix, mulTimes):
    if mulTimes==1: 
        newMatrix=[[0 for _ in range(a)] for _ in range(a)]
        for rowId in range(a):
            for colId in range(a):
                newMatrix[rowId][colId]=matrix[rowId][colId]%1000
        return newMatrix
    
    elif mulTimes==2: 
        return getMulMatrix(matrix, matrix)
                
    else:
        devidedMulMatrix=getPowMatrix(matrix, mulTimes//2)
        squareMulMatrix=getPowMatrix(devidedMulMatrix, 2)
        if mulTimes%2==0: return squareMulMatrix
        else: 
            return getMulMatrix(squareMulMatrix, matrix)

def getMulMatrix(matrix_a, matrix_b):
    newMatrix=[[0 for _ in range(a)] for _ in range(a)]
    for rowId in range(a):
        for colId in range(a):
            for idx in range(a):
                newMatrix[rowId][colId]+=matrix_a[rowId][idx]*matrix_b[idx][colId]
                newMatrix[rowId][colId]%=1000
    return newMatrix

for i in getPowMatrix(matrix, b):
    print(*i)