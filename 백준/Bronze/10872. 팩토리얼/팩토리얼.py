N=int(input())

def factorial(N):
    if N<=1: return 1
    elif N==2: return 2
    elif N>=3: return factorial(N-1)*N

print(factorial(N))