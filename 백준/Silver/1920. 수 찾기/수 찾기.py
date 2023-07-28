import sys

n=int(input())
nList=sorted(map(int, sys.stdin.readline().split()))
m=int(input())

def checkNum():
    for num in tuple(map(int,sys.stdin.readline().split())):
        # if num==1: break
        binarySearch(num)
        
def binarySearch(num):
    leftId=0
    rightId=n-1

    while (leftId<=rightId):
        midId=(leftId+rightId)//2
        if nList[midId]==num: return print(1)
        else:
            if num<nList[midId]: rightId=midId-1
            elif num>nList[midId]: leftId=midId+1
    
    return print(0)

checkNum()