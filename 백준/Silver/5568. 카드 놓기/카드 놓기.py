n=int(input())
k=int(input())
cards=[input() for _ in range(0, n)]

permCards=[]
idxArr=[0]*(n+1)

def makePermCards(k, string_, idxArr):
    if k==0: permCards.append(string_)
    elif k>0:
        for idx in range(0, n):
            if idxArr[idx]==0:
                new_idxArr=idxArr.copy()
                new_idxArr[idx]=1
                makePermCards(k-1, string_+cards[idx], new_idxArr)

makePermCards(k, '', idxArr)

print(len(set(permCards)))
