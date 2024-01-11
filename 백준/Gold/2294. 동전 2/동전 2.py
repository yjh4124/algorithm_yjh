
import sys
from collections import deque

input = sys.stdin.readline

def getMinNumCoin(coins, k):
    queue = deque([(0, 0)]) 
    visited = [False] * (k + 1)

    while queue:
        current_sum, coin_count = queue.popleft()

        for coin in coins:
            next_sum = current_sum + coin

            if next_sum == k:
                return coin_count + 1

            if next_sum < k and not visited[next_sum]:
                visited[next_sum] = True
                queue.append((next_sum, coin_count + 1))

    return -1

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

print(getMinNumCoin(coins, k))
