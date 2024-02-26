import sys

input=sys.stdin.readline

n=int(input())

nums=input().strip()
summ=0

for i in nums:
    summ+=int(i)
    
print(summ)