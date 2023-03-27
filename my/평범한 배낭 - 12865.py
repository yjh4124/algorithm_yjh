n, k = map(int, input().split())

backpack=[]

for idx in range(n):
    backpack.append(tuple(map(int, sys.stdin.readline().split())))

backpack.sort(key=lambda x:(x[0], x[1]))

# print(backpack)

t_weight=[[] for _ in range(k+1)]

for w, v in backpack:
    t_weight[w].append([v, (w, v)])

# print(t_weight)

for w, v in backpack:
    for idx in range(w+1, k+1):
        for pack in t_weight[idx]:
            if (w,v) not in pack and idx+w<=k:
                temp=[pack[0]]+sorted(pack[1:]+[(w,v)])
                
                temp[0]+=v
                if temp not in t_weight[idx+w]:
                    t_weight[idx+w].append(temp)

print(t_weight)
while [] in t_weight:
    t_weight.remove([])
print(max(list(map(max, t_weight)))[0])
