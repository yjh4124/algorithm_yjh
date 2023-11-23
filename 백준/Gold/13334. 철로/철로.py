import sys

sys.setrecursionlimit(10**8)
input = sys.stdin.readline


import heapq

n = int(input())
trains = []

for _ in range(n):
    start, end = map(int, input().split())
    trains.append((min(start, end), max(start, end)))

d = int(input())
trains.sort(key=lambda x: x[1])
min_heap = []
count = 0

for train in trains:
    while min_heap and train[1] - min_heap[0] > d:
        heapq.heappop(min_heap)

    if train[1] - train[0] <= d:
        heapq.heappush(min_heap, train[0])
        count = max(count, len(min_heap))

print(count)
