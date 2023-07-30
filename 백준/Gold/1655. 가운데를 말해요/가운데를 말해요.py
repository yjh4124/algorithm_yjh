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

    if heapR and -heapL[0]>heapR[0]:
        heapq.heappush(heapR, -heapq.heappop(heapL))
        heapq.heappush(heapL, -heapq.heappop(heapR))
    print(-heapL[0])

for _ in range(n):
    getMidNum()