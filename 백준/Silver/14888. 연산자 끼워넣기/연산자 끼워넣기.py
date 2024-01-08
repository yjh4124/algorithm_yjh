
import sys

input = sys.stdin.readline
INF = int(1e9)


def getRes(operators, digitIdx, lastCalcRes):
    global maxRes, minRes
    for operatorIdx in range(4):
        if operators[operatorIdx] >= 1:
            nextCalcRes = getNextCalcRes(lastCalcRes, digitIdx, operatorIdx)
            if digitIdx == n - 1:
                maxRes = max(maxRes, nextCalcRes)
                minRes = min(minRes, nextCalcRes)
            operators[operatorIdx] -= 1
            if digitIdx != n:
                getRes(operators, digitIdx + 1, nextCalcRes)
            operators[operatorIdx] += 1


def getNextCalcRes(lastCalcRes, digitIdx, operatorIdx):
    if operatorIdx == 0:
        nextCalcRes = lastCalcRes + digitsA[digitIdx]
    elif operatorIdx == 1:
        nextCalcRes = lastCalcRes - digitsA[digitIdx]
    elif operatorIdx == 2:
        nextCalcRes = lastCalcRes * digitsA[digitIdx]
    elif operatorIdx == 3:
        nextCalcRes = (
            abs(lastCalcRes) // digitsA[digitIdx] * (1 if lastCalcRes >= 0 else -1)
        )

    return nextCalcRes


n = int(input())
digitsA = [int(i) for i in input().split()]
operators = [int(i) for i in input().split()]  # +, -, x, /

maxRes = -INF
minRes = INF
getRes(operators, 1, digitsA[0])

print(maxRes)
print(minRes)