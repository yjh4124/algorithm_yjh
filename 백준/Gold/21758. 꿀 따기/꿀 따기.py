import sys
from math import inf

n=int(input())

data=[int(data) for data in sys.stdin.readline().split()]

init_honey= sum(data)*2-data[0]*2-data[1]

throw_honey=0
min_throw_honey=inf

total_get_honey=[]


for idx in range(1, n-1):
    
    if idx>=2: throw_honey-=data[idx-1]
    if idx==1: throw_honey=data[idx]
    if idx>=2: throw_honey+=data[idx]*2

    min_throw_honey=min(min_throw_honey, throw_honey)

total_get_honey.append(init_honey-min_throw_honey)

data_reverse=list(reversed(data))
# print(data_reverse)
init_honey2= sum(data_reverse)*2-data_reverse[0]*2-data_reverse[1]
throw_honey=0
min_throw_honey=inf

for idx in range(1, n-1):
    
    if idx>=2: throw_honey-=data_reverse[idx-1]
    if idx==1: throw_honey=data_reverse[idx]
    if idx>=2: throw_honey+=data_reverse[idx]*2

    min_throw_honey=min(min_throw_honey, throw_honey)
    
    

total_get_honey.append(init_honey2-min_throw_honey)


max_honey_bin=0

init_honey3=sum(data)-data[0]-data[n-1]
max_honey_bin=max(data[1:n-1])

total_get_honey.append(init_honey3+max_honey_bin)

print(max(total_get_honey))

