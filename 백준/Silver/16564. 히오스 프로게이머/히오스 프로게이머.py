
import sys

input = sys.stdin.readline


def getMinimumTeamLevel(x_levels, k_level):
    sorted_levels = sorted(x_levels)
    minLevel = min(sorted_levels)
    maxLevel = max(sorted_levels) + k_level
    mid = (minLevel + maxLevel) // 2

    while minLevel <= maxLevel:
        sum = 0
        for level in x_levels:
            if mid > level:
                sum += mid - level
                if sum > k_level:
                    break

        if sum > k_level:
            maxLevel = mid - 1
        elif sum < k_level:
            minLevel = mid + 1
        elif sum == k_level:
            break

        mid = (minLevel + maxLevel) // 2

    tLevel = mid

    return tLevel


n, k = map(int, (input().split()))
x_levels = [int(input().strip()) for _ in range(n)]

tLevel = getMinimumTeamLevel(x_levels, k)

print(tLevel)
