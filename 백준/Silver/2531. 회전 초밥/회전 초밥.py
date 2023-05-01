import sys


n, d, k, c= map(int, sys.stdin.readline().split())

data_og=[int(i.strip()) for i in sys.stdin.readlines()]

data=data_og+data_og[:k-1]

# print(data)

check_arr=[0 for _ in range(d+1)]
idx=0
cnt=0
result=[]
max_res=0

while idx<k:
    if check_arr[data[idx]]==0:
        cnt+=1
    check_arr[data[idx]]+=1
    
    idx+=1
        
if check_arr[c]==0:
    # result.append(cnt+1)
    max_res=max(max_res, cnt+1)
elif check_arr[c]!=0:
    # result.append(cnt)
    max_res=max(max_res, cnt)

# print(result)

while (idx<n+k-1):
    if check_arr[data[idx-k]]==1:
        cnt-=1
    check_arr[data[idx-k]]-=1

    if check_arr[data[idx]]==0:
        cnt+=1
    check_arr[data[idx]]+=1

    if check_arr[c]==0:
        # result.append(cnt+1)
        max_res=max(max_res, cnt+1)
    elif check_arr[c]!=0:
        # result.append(cnt)
        max_res=max(max_res, cnt)

    idx+=1

# print(result)
print(max_res)
