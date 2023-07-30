import sys
n=int(input())

def countLookedStick():
    stack=[]
    for _ in range(n):
        stick=int(sys.stdin.readline())
        while stack and stack[-1]<=stick:
            stack.pop()
        stack.append(stick)

    return print(len(stack))

countLookedStick()