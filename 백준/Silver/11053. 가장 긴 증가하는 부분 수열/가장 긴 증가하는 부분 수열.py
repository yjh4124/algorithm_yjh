import sys

n=int(input())

seq=[int(i) for i in  input().split()]
# print(seq)

result=(0,)
result=[]

subseq=[[0,[]] for _ in range(n)]

for idx in range(n):
    if idx==0:
        subseq[idx][0]+=1
        subseq[idx][1]+=[seq[idx]]
        result=subseq[idx][0]
    elif idx!=0:
        for pre_idx in range(idx):
            if seq[idx]>subseq[pre_idx][1][-1]:
                if(subseq[idx][0]<subseq[pre_idx][0]+1):
                    subseq[idx][0]=subseq[pre_idx][0]+1
                    subseq[idx][1]=subseq[pre_idx][1]+[seq[idx]]
        if subseq[idx][0]==0:
            subseq[idx][0]+=1
            subseq[idx][1]+=[seq[idx]]
        if result<subseq[idx][0]:
            result=subseq[idx][0]

print(result)
# print(subseq)