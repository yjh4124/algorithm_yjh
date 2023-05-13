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
# print(sum_)
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
        # print(min_,max_,mid, checksum)
        # print(mid, checksum)
        if checksum<m:
            if (min_+mid)//2!=min_:
                min_=(min_+mid)//2
            else:
                min_=(min_+mid)//2+1

        elif checksum>m:
            max_=(mid+max_)//2
            
        elif checksum==m:
            break
    
    print(mid)
            



