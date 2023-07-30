n=int(input())

for i in range(n):
    ps=list(input())
    cnt=0
    init=0
    for j in ps:
        if init==0:
            if j=='(':
                cnt+=1
                init=1
            else: 
                print('NO')
                break
        else:
            if j=='(':
                cnt+=1
                init=1
            elif j==')':
                if cnt!=0:
                    cnt-=1
                else:
                    print('NO')
                    break
    else:
        if cnt==0:
            print('YES')
        else: 
            # print(1)
            print('NO')