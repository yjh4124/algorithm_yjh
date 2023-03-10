from math import sqrt, ceil
import time

# start = time.time()

n = 10000  # 2부터 1000까지 모든 수에 대하여 소수를 찾을 것이다.
# 0,1을 제외한 모든 숫자가 소수(True)인 것으로 설정하고 시작한다.
array = [True for i in range(n + 1)]

# 에라토스테네스의 체 알고리즘
for i in range(2, int(sqrt(n)) + 1):  # 2부터 n의 제곱근까지의 모든 수를 확인
    if array[i] == True:  # i가 소수인 경우
        # i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

# 모든 소수 출력
primels=[]
for i in range(2, n+1):
    if array[i]:
        primels.append(i)

# print(primels)


n = int(input())

for i in range(0, n):
    num = int(input())
    half = num//2
    for j in range(half, 1, -1):
        if (j in primels) and (num-j in primels):
            print(j, num-j)
            break