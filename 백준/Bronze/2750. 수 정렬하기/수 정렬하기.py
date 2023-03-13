n=int(input())

ls=[int(input()) for i in range(n)]

# print(ls)

for i in range(n):
    for j in range(i+1):
        if ls[j]>ls[i]:
            temp=ls[i]
            for k in range(i,j-1,-1):
                ls[k]=ls[k-1]
            ls[j]=temp

# print(ls)
for i in ls:
    print(i)