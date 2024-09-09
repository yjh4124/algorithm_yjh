import sys

input = sys.stdin.readline

class SegmentTree:
    # 구간합 세그먼트 트리 생성
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (2 * self.n)
        # 단일 구간 기저노드 구간합 할당
        for i in range(self.n):
            self.tree[self.n + i] = nums[i]
        # 하위 구간부터 상위 구간으로 구간합 초기화
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    # 구간합 수정
    def update(self, pos, value):
        pos += self.n
        self.tree[pos] = value
        # 하위 구간부터 상위 구간으로 구간합 수정
        while pos > 1:
            pos //= 2
            self.tree[pos] = self.tree[2 * pos] + self.tree[2 * pos + 1]

    # 구간합 계산
    def range_sum(self, left, right):
        left += self.n
        right += self.n + 1
        sum_ = 0
        while left < right:
            if left % 2 == 1:
                sum_ += self.tree[left]
                left += 1
            if right % 2 == 1:
                right -= 1
                sum_ += self.tree[right]
            left //= 2
            right //= 2

        return sum_


n, change_ops, sum_ops = map(int, input().split())

nums = [int(input()) for _ in range(n)]

seg_tree = SegmentTree(nums)

for _ in range(change_ops + sum_ops):
    method, arg1, arg2 = map(int, input().split())

    if method == 1:
        seg_tree.update(arg1 - 1, arg2)
    else:
        print(seg_tree.range_sum(arg1 - 1, arg2 - 1))
