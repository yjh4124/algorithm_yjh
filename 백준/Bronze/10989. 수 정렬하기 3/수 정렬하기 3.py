import sys

n=int(input())

def ascendingOrder(n):
    numList=[0]*10001
    for _ in range(n):
        numList[int(sys.stdin.readline())]+=1
    
    for idx in range(0,10001):
        if numList[idx]!=0: 
            for _ in range(numList[idx]): print(idx)

ascendingOrder(n)