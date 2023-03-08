n=int(input())
k=int(input())
card=[]
for i in range(0,n):
    card.append(int(input()))

# print(card)

# print(list(range(0,n)[::-1]))
idls=[]
tpidls=[]

idval=[0 for i in range(0,k)]

# if -1 not in idval:
#     print(idval[0])

idset=[]
def cardpic(cdn, rek, precnt, cnt, idval,roof):
    for i in range(0,cdn+1)[::-1]:
        # roof+=1
        # print('----')
        idval[precnt-1]=i-1
        # print(idval)
        if i==0: 
            cnt=cnt-1
            # print(1)
            continue
        else: cnt=precnt
        # if cnt<rek: cnt+=1  
        if -1 not in idval:
            if (idval not in idset):
                if len(set(idval))==rek:
                    templs=[]
                    for i in idval:
                        templs.append(i)
                    idset.append(templs)
                    # print(tuple(templs))
        if cnt<rek: 
            cnt+=1

            # print(roof)
            cardpic(cdn, rek, precnt+1, cnt, idval,roof)


# cardpic(n, k, 1, idval,0)
cardpic(n, k, 1, 1, idval,0)


# print(idset)

idlist = idset
for i in idlist:
    if i[::-1] not in idlist: idlist.append(i[::-1])
# print(idlist)

numls=[]
for j in idlist:
    temp=''
    for k in j:
        temp+=str(card[k])
    # print(temp)
    numls.append(temp)

# print(numls)
realnumls=set(numls)

# print(realnumls)
print(len(realnumls))