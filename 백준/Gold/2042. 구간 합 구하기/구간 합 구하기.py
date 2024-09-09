import sys

input = sys.stdin.readline

import math


class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        # 세그먼트 트리 깊이 및 원소 갯수 설정
        height = math.ceil(math.log2(self.n))
        max_size = 2 ** (height + 1) - 1

        # 트리 원소 초기화
        self.tree = [0] * max_size

        # 구간합 설정
        self.build_bottom_up(nums)

    # 단일 구간 기저 노드부터 구간합 값 설정
    def build_bottom_up(self, nums):
        # 기저 노드 인덱스 오프셋
        offset = 2 ** math.ceil(math.log2(self.n)) - 1

        # 기저 노드 구간합 설정
        for i in range(self.n):
            self.tree[offset + i] = nums[i]

        # 하위 구간합 노드부터 상위 구간합 노드 설정
        for i in range(offset - 1, -1, -1):
            self.tree[i] = self.tree[2 * i + 1] + self.tree[2 * i + 2]

    # 구간합 수정
    def update(self, index, value):
        # 기저 원소 인덱스 설정
        offset = 2 ** math.ceil(math.log2(self.n)) - 1
        pos = offset + index
        self.tree[pos] = value

        # 기저 원소부터 상위 원소로 구간합 수정
        while pos > 0:
            pos = (pos - 1) // 2
            self.tree[pos] = self.tree[2 * pos + 1] + self.tree[2 * pos + 2]

    def range_sum(self, left, right):
        return self.range_sum_query(
            0, 0, 2 ** math.ceil(math.log2(self.n)) - 1, left, right
        )

    # 구간합 계산
    def range_sum_query(self, node, start, end, left, right):
        # 구간이 일치할 경우
        if left <= start and end <= right:
            return self.tree[node]

        # 구간을 벗어난 경우
        if right < start or left > end:
            return 0

        # 구간이 중심 노드를 기준으로 분할되는 경우
        mid = (start + end) // 2
        left_sum = self.range_sum_query(2 * node + 1, start, mid, left, right)
        right_sum = self.range_sum_query(2 * node + 2, mid + 1, end, left, right)
        return left_sum + right_sum


n, change_ops, sum_ops = map(int, input().split())

nums = [int(input()) for _ in range(n)]

seg_tree = SegmentTree(nums)

for _ in range(change_ops + sum_ops):
    method, arg1, arg2 = map(int, input().split())
    if method == 1:
        seg_tree.update(arg1 - 1, arg2)
    else:
        print(seg_tree.range_sum(arg1 - 1, arg2 - 1))
