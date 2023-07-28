import sys
from collections import Counter

n, m=map(int, input().split())
trees=Counter(map(int, sys.stdin.readline().split()))

def setHeight():
    lowHeight=0
    highHeight=max(trees)

    while lowHeight<=highHeight:
        midHeight=(lowHeight+highHeight)//2
        
        if getTrees(midHeight)==m: return print(midHeight)
        else:
            if getTrees(midHeight)>m: 
                lowHeight=midHeight+1
            else: highHeight=midHeight-1
        
    return print(highHeight)

def getTrees(height):
    total=0
    for tree, cnt in trees.items():
        if tree>height: total+=(tree-height)*cnt

    return total

setHeight()
