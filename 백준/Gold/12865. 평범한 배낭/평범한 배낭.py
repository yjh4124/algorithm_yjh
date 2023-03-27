import sys

n, k = map(int, input().split())

backpack=[]

for idx in range(n):
    backpack.append(tuple(map(int, sys.stdin.readline().split())))

backpack.sort(key=lambda x:(x[0], x[1]))

# print(backpack)

t_weight=[0 for _ in range(k+1)]

for w, v in backpack:
    for idx in range(k, w-1, -1):
        if t_weight[idx]<t_weight[idx-w]+v:
            t_weight[idx]=t_weight[idx-w]+v


# print(t_weight)

print(t_weight[-1])