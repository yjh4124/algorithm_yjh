import sys

k=int(input())
c=int(input())

data=[[int(data) for data in sys.stdin.readline().split()]
    for _ in range(c)]

for m, n in data:

    round=max(m, n)
    if round<=1: 
        print(1)
    elif round>1:
        max_diff=k-round
        if m>=n:
            if abs(m-n)>max_diff+2: print(0)
            elif abs(m-n)<=max_diff+2: print(1)
        elif m<n:
            if abs(m-n)>max_diff+1: print(0)
            elif abs(m-n)<=max_diff+1: print(1)
    