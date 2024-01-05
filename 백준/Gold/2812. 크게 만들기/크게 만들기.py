import sys

input = sys.stdin.readline


def getMaxNum(num, n, k):
    stack = []

    for digit in num:
        while stack and k > 0 and stack[-1] < digit:
            stack.pop()
            k -= 1

        stack.append(digit)

    if k > 0:
        maxNum = "".join(stack[:-k])
    else:
        maxNum = "".join(stack)

    return maxNum


n, k = map(int, input().split())
num = input().strip()

maxNum = getMaxNum(num, n, k)

print(maxNum)
