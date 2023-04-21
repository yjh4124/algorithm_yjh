import sys
from math import inf

n=int(input())

data_og=[int(i)%2 for i in sys.stdin.readline().split()]

# print(data)

res=inf

for init_val in range(2):
    insert_idx=0
    cnt=0
    check=0
    data=data_og.copy()

    if init_val==data[0]:
        for idx in range(n):
            if data[idx]==init_val:
                continue

            elif data[idx]!=init_val:
                temp=data[insert_idx]
                data[insert_idx]=data[idx]
                data[idx]=temp
                cnt+=idx-insert_idx
                insert_idx+=1
                # print(data)
        # print(cnt)

    if init_val!=data[0]:
        for idx in range(n):
            if data[idx]==init_val:
                insert_idx=idx
                break
        

        for idx in range(insert_idx, n):
            if data[idx]==init_val:
                continue

            elif data[idx]!=init_val:
                temp=data[insert_idx]
                data[insert_idx]=data[idx]
                data[idx]=temp
                cnt+=idx-insert_idx
                insert_idx+=1
                # print(data)

    res=min(res,cnt)
    

print(res)