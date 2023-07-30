import heapq
import sys

n=int(input())
heap=[]

def heapPop():
    if heap: print(-heapq.heappop(heap))
    else: print(0)

def heapPush(num):
    heapq.heappush(heap, num)
    
for _ in range(n):
    num= int(sys.stdin.readline())
    if num==0: heapPop()
    else: heapPush(-num)