t=int(input())

for _ in range(t):
    n=int(input())
    coin=[int(i) for i in input().split()]
    m=int(input())

    sol=[0 for _ in range(m+1)]
    
    # for i in coin:
    #     if i<=m:
    #         sol[i]+=1
    sol[0]=1
    
    for pic in coin:
        for idx_sol in range(pic,m+1):
            # if idx_sol+pic<=m:
            sol[idx_sol]+=sol[idx_sol-pic]

    print(sol[m])