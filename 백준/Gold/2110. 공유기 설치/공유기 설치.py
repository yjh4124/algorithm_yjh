import sys

n, c=map(int, input().split())
houses=sorted([int(sys.stdin.readline()) for _ in range(n)])

def getDistance():
    shortDist=1
    longDist=houses[n-1]

    while shortDist<=longDist:
        midDist=(shortDist+longDist)//2
        if checkRouterNum(midDist)>=c: shortDist=midDist+1
        else: longDist=midDist-1

    return print(longDist)

def checkRouterNum(minDistance):
    lastHouseLoc=houses[0]
    count=1

    for presentHouseLoc in houses:
        diffDist=presentHouseLoc-lastHouseLoc
        if diffDist>=minDistance: 
            count+=1
            lastHouseLoc=presentHouseLoc 
    
    return count

getDistance()
