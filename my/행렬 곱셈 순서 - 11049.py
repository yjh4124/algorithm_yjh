from math import inf

n=int(input())

matrix=[]
data=[]

for i in range(n):
    r, c=map(int, input().split())
    matrix.append((r, c))
    if i!=n-1:
        data.append(r)
    elif i==n-1:
        data.append(r)
        data.append(c)

result=inf

def mul(visit, res):
    global result
    for idx in range(1,n):
        if visit[idx]==0:
            for l in range(idx-1, -1, -1):
                if visit[l]==0:
                    left_idx=l
                    break
            for r in range(idx+1, n+1):
                if visit[r]==0:
                    right_idx=r
                    break
            new_res=res+data[left_idx]*data[idx]*data[right_idx]
            new_visit=visit.copy()
            new_visit[idx]=1
            if 0 in new_visit[1:n]:
                mul(new_visit, new_res)
                
            elif 0 not in new_visit[1:n]:
                if new_res<result:
                    result=new_res
                    

mul([0 for _ in range(n+1)], 0)

print(result)
