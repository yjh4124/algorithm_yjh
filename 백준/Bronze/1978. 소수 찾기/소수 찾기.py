n=int(input())

numlist=list(map(int, input().split()))

count=0

for i in numlist:
    checknum=0
    for j in range(1,i+1):
        if i%j==0: checknum+=1
    if checknum==2:
        count+=1
        
print(count)
