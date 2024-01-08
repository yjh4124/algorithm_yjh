import sys

input = sys.stdin.readline

def getTimeEndIceberg(n, m, iceberg):
    timeEnd = 0
    iceberg_cells = [(i, j) for i in range(n) for j in range(m) if iceberg[i][j]]
    
    while True:
        numIceberg = getNumIceberg(n, m, iceberg)
        if numIceberg >= 2:
            break
        if numIceberg == 0:
            timeEnd = 0
            break
        timeEnd += 1
        meltIceberg(n, m, iceberg, iceberg_cells)

    return timeEnd

def meltIceberg(n, m, iceberg, iceberg_cells):
    melting = []
    for i, j in iceberg_cells:
        cnt = 0
        for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= ni < n and 0 <= nj < m and not iceberg[ni][nj]:
                cnt += 1
        if cnt > 0:
            melting.append((i, j, cnt))

    for i, j, cnt in melting:
        iceberg[i][j] = max(iceberg[i][j] - cnt, 0)
        if iceberg[i][j] == 0:
            iceberg_cells.remove((i, j))

def getNumIceberg(n, m, iceberg):
    numIceberg = 0
    group = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if iceberg[i][j] and not group[i][j]:
                numIceberg += 1
                if numIceberg >= 2:
                    return numIceberg
                makeGroupIceberg(n, m, i, j, iceberg, group, numIceberg)
    return numIceberg

def makeGroupIceberg(n, m, ci, cj, iceberg, group, numIceberg):
    stack = [(ci, cj)]
    while stack:
        i, j = stack.pop()
        if group[i][j]:
            continue
        group[i][j] = numIceberg
        for ni, mj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= ni < n and 0 <= mj < m and iceberg[ni][mj] and not group[ni][mj]:
                stack.append((ni, mj))

n, m = map(int, input().split())

iceberg = []

for _ in range(n):
    iceberg.append([int(i) for i in input().split()])

timeEnd = getTimeEndIceberg(n, m, iceberg)
print(timeEnd)
