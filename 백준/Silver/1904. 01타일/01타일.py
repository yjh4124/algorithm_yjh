n=int(input())

num=[1,2]

if n==1: print(num[0])

elif n==2: print(num[1])

elif n>2: 
    while len(num)<n:
        num.append((num[-1]+num[-2])%15746)

if n>2:
    print(num[-1])