import sys

n=int(input())

def ascendingOrder(n):
    numList=[0]*2000001
    for _ in range(n):
        numList[int(sys.stdin.readline())+1000000]+=1
    
    for idx in range(0,2000001):
        if numList[idx]!=0: 
            for _ in range(numList[idx]): print(idx-1000000)

ascendingOrder(n)