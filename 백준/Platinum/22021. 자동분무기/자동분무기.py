import sys

m=int(input())

data=[[int(data) for data in sys.stdin.readline().split()]
    for _ in range(8)]

spray=[[0 for _ in range(8)] for _ in range(8)]
standard_data=[[0 for _ in range(8)] for _ in range(8)]

for row in range(8):
    for col in range(8):
        standard_data[row][col]=data[row][col]-m

# for i in data:
#     print(i)
# print()
# for i in standard_data:
#     print(i)
# print()
# for i in spray:
#     print(i)

sum_total=0
for row in range(8):
    for col in range(8):
        standard_data[row][col]=data[row][col]-m
        sum_total+=standard_data[row][col]


cnt=0
idx=64
for row in range(8):
    if cnt>idx: break
    for col in range(8):
        if cnt>idx: 
            # print(sum_1, sum_2, sum_3)
            break
        sum_1=0

        for r in range(8):
            if r!=row:
                sum_1+=standard_data[r][col]
        for c in range(8):
            if c!=col:
                sum_1+=standard_data[row][c]
        sum_1+=standard_data[row][col]

        sum_2=sum_total-sum_1
        sum_3=standard_data[row][col]

        spray[row][col]=(13*sum_1-2*sum_2-90*standard_data[row][col])/(109)
        cnt+=1

# print()
# for i in spray:
#     print(i)

# print()
for row in range(8):
    for col in range(8):
        if spray[row][col]>0:
            print('+ ', end='')
        elif spray[row][col]<0:
            print('- ', end='')
        else:
            print('. ', end='')
    print()