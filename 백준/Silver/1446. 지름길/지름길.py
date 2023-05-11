import sys
from math import inf
n, d=map(int, input().split())

# print(n, d)

data=[[int(data) for data in sys.stdin.readline().split()]
      for _ in range(n)]

data.sort()
# for i in data:
#     print(i)

result=[]
res_min=inf

def dfs(start, driving_cost, idx):
    global res_min
    
    if start==d:
        res_min=min(res_min, driving_cost)
        result.append(driving_cost)
        return
    elif start>d:
        return
    # elif idx>=n and start<d:
    #     next_start=d
    #     next_driving_cost=driving_cost+d-start
    #     res_min=min(res_min, driving_cost)
    #     result.append(driving_cost)
    #     return

    while (idx<n):

        if (start>data[idx][0]):
            idx+=1
        elif (start==data[idx][0]):
            
            if (data[idx][1]-data[idx][0]>=data[idx][2]):
                next_start=data[idx][1]
                next_driving_cost=driving_cost+data[idx][2]
                next_idx=idx+1
                dfs(next_start, next_driving_cost, next_idx)
                # start=start+data[idx+1][0]-data[idx][0]
                # driving_cost=driving_cost+data[idx+1][0]-data[idx][0]
                idx=idx+1

            elif (data[idx][1]-data[idx][0]<data[idx][2]):
                idx+=1

        elif (start<data[idx][0]):
            next_start=data[idx][0]
            next_driving_cost=driving_cost+data[idx][0]-start
            next_idx=idx
            dfs(next_start, next_driving_cost, next_idx)
            idx+=1

    if start<d:
        driving_cost=driving_cost+d-start
        # result.append(driving_cost)
        res_min=min(res_min, driving_cost)
        
        return

# start=0
# driving_cost=0
# idx=0

# dfs(start, driving_cost, idx)
dfs(0,0,0)

# print(result)
print(res_min)
