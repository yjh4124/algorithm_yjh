import sys

n=int(input())

def fibo(pre, now, n):
    if n!=0:
        n-=1
        fibo(now, pre+now, n)
    elif n==0:
        print(pre)

fibo(0, 1, n)