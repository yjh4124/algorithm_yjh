import sys

n=int(input())

data=[int(data) for data in sys.stdin.readline().split()]

m=int(input())

data.sort()

# print(n, m)
# print(data)

sum_=sum(data)
min_=0
max_=data[-1]

if sum_<=m:
    print(data[-1])

elif sum_>m:
    while(min_<max_):
        
        checksum=0
        mid=(min_+max_)//2

        for elem in data:
            if elem>mid:
                checksum+=mid
            elif elem<=mid:
                checksum+=elem
        # print(mid, checksum)
        if checksum<m:
            if min_!=mid:
                min_=mid
            else:
                min_=mid+1

        elif checksum>m:
            max_=mid
            
        elif checksum==m:
            break
    
    print(mid)
            



