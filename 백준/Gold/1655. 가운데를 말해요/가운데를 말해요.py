from collections import deque
import heapq
import sys

n=int(input())
heapL=[]
heapR=[]

def getMidNum():
    num=int(sys.stdin.readline())
    if len(heapL)==len(heapR): heapq.heappush(heapL, -num)
    else: heapq.heappush(heapR, num)

    if not heapL: print(heapR[0])
    elif not heapR: print(-heapL[0])
    else:
        tempL=-heapq.heappop(heapL)
        tempR=heapq.heappop(heapR)
        if tempL>tempR:
            heapq.heappush(heapR, tempL)
            heapq.heappush(heapL, -tempR)
        else:
            heapq.heappush(heapR, tempR)
            heapq.heappush(heapL, -tempL)
            
        print(min(-heapL[0], heapR[0]))

for _ in range(n):
    getMidNum()