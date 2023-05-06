import sys

data=list(input())

# print(data)

check=[0 for _ in range(26)]
cnt=[0 for _ in range(26)]

for elem in data:
    idx=ord(elem)-ord('A')
    
    if check[idx]==0:
        check[idx]+=1
    elif check[idx]!=0:
        check[idx]-=1
        cnt[idx]+=1

pivot=-1
str_left=[]
if len(data)%2==sum(check):
    for j in range(26):
        if check[j]==1:
            pivot=j
    for i in range(26):
        for _ in range(cnt[i]):
            str_left+=chr(i+ord('A'))

    print(''.join(str_left),end='')
    if pivot!=-1: print(chr(pivot+ord('A')),end='')
    print(''.join(reversed(str_left)),end='')

elif len(data)%2!=sum(check):
    print("I'm Sorry Hansoo")


# print(check)
# print(cnt)
