col, row= map(int,input().split())
T=int(input())

def getMaxArea(col, row, T):
    colArr= [0]*(col+1)
    rowArr= [0]*(row+1)
    colArr[0], colArr[col]=1, 1
    rowArr[0], rowArr[row]=1, 1

    for _ in range(0, T):
        numDirection, cutId=map(int, input().split())
        if numDirection==0: rowArr[cutId]=1
        elif numDirection==1: colArr[cutId]=1

    return print(maxLen(colArr)*maxLen(rowArr))

def maxLen(array):
    maxLen=0
    addLen=1

    for id in array:
        if id==0: addLen+=1
        elif id==1: 
            maxLen=max(maxLen, addLen)
            addLen=1

    return maxLen

getMaxArea(col, row, T)


