# 입력 받기
M, N, L = map(int, input().split())
gun_positions = list(map(int, input().split()))
animals = []

for _ in range(N):
    x, y = map(int, input().split())
    if y <= L:
        animals.append((x, y))

# 사대 위치 정렬
gun_positions.sort()

# 사냥 결과 초기화
result = 0

# 각 동물에 대해 가장 가까운 사대 찾기
for x, y in animals:
    left, right = 0, M - 1
    while left <= right:
        mid = (left + right) // 2
        dist = abs(x - gun_positions[mid]) + y  # 사대와 동물 사이의 거리 계산

        if dist <= L:
            result += 1
            break  # 이미 사냥할 수 있는 사대를 찾았으므로 종료
        elif x < gun_positions[mid]:
            right = mid - 1
        else:
            left = mid + 1

# 결과 출력
print(result)
