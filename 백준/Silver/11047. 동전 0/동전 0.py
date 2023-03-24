import sys

n, k= map(int,sys.stdin.readline().split())

coins=[]
for _ in range(n):
    coins.append(int(input()))

num=0
total=0
for idx in range(len(coins)-1,-1,-1):
    if coins[idx]<=(k-total):
        num+=((k-total)//coins[idx])
        total+=coins[idx]*((k-total)//coins[idx])
        # print(total)
    # else: print(0)

    if total==k: break

print(num)