import sys
import heapq

input = sys.stdin.readline


def getMaxNumRoute(routes, d):
    maxNumRoute = 0
    leftHeap = []

    for left, right in routes:
        while leftHeap and right - leftHeap[0] > d:
            heapq.heappop(leftHeap)
        
        if right - left <= d:
            heapq.heappush(leftHeap, left)
            maxNumRoute = max(maxNumRoute, len(leftHeap))

    return maxNumRoute


n = int(input())
routes = [sorted(map(int, input().split())) for _ in range(n)]
routes.sort(key=lambda x: x[1])
d = int(input())

maxNumRoute = getMaxNumRoute(routes, d)
print(maxNumRoute)
