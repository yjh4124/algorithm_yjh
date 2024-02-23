import sys

input = sys.stdin.readline

n = int(input())

num=n

for i in range(2,int(n**0.5)+1):
    while num%i==0:
        print(i)
        num//=i
    if num==1 or num<i : break

if num!=1: print(num)
    