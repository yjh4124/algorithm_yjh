
import sys

input = sys.stdin.readline

INF = 10**9
block_num = int(input())
blocks = list(input().rstrip())

energy_memo = [INF] * block_num
energy_memo[0] = 0


# 점프 가능한 블록 확인
def is_possible_next_block(i, j):
    now = blocks[i]
    next_ = blocks[j]
    if (
        (now == "B" and next_ == "O")
        or (now == "O" and next_ == "J")
        or (now == "J" and next_ == "B")
    ):
        return True
    return False


# 점프 가능하면, 에너지 메모
for i in range(block_num):
    for j in range(i + 1, block_num):
        if is_possible_next_block(i, j):
            energy_memo[j] = min(energy_memo[j], energy_memo[i] + (j - i) ** 2)

result = energy_memo[block_num - 1]
print(result if result != INF else -1)
