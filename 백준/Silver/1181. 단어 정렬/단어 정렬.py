import sys

n=int(input())
strLenList=[[] for _ in range(51)]
for _ in range(n):
    word=sys.stdin.readline().strip()
    strLenList[len(word)].append(word)

def mergeSort(array):
    if len(array)>=2:
        leftArr=mergeSort(array[:len(array)//2])
        rightArr=mergeSort(array[len(array)//2:len(array)])
        return merge(leftArr, rightArr)
    
    elif len(array)<=1:
        return array

def merge(leftArr, rightArr):
    leftlen=len(leftArr)
    rightlen=len(rightArr)

    leftId=0
    rightId=0

    mergeArr=[]

    while leftId<leftlen and rightId<rightlen:
        for idx in range(len(leftArr[leftId])):
            if ord(leftArr[leftId][idx])<ord(rightArr[rightId][idx]):
                mergeArr.append(leftArr[leftId])
                leftId+=1
                break
            elif ord(leftArr[leftId][idx])>ord(rightArr[rightId][idx]):
                mergeArr.append(rightArr[rightId])
                rightId+=1
                break
            elif ord(leftArr[leftId][idx])==ord(rightArr[rightId][idx]) and (idx==len(leftArr[leftId])-1):
                mergeArr.append(leftArr[leftId])
                leftId+=1
                rightId+=1

    while leftId<leftlen:
        mergeArr.append(leftArr[leftId])
        leftId+=1

    while rightId<rightlen:
        mergeArr.append(rightArr[rightId])
        rightId+=1

    return mergeArr

for strList in strLenList:
    if len(strList)!=0:
        for i in mergeSort(strList):
            print(i)
