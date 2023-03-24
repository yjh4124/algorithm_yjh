n = int(input())
 
li = [1,2]
 
for i in range(2,n):
    li.append((li[i-1]+li[i-2])%15746)
print(li[n-1])