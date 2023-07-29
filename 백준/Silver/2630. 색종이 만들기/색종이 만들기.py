import sys

n= int(input())
papers=tuple(tuple(map(int, sys.stdin.readline().split())) for _ in range(n))

colorPaper=[0,0]

def devidePapers(rowStart, rowEnd, colStart, colEnd):
    global colorPaper
    
    initColor=papers[rowStart][colStart]
    boolPaper=0

    for rowId in range(rowStart, rowEnd):
        if boolPaper==1: break
        for colId in range(colStart, colEnd):
            if papers[rowId][colId]!=initColor: 
                boolPaper=1
            if boolPaper==1: break

    if boolPaper==0: colorPaper[initColor]+=1
    else: 
        if(rowEnd-rowStart)//2>=1 and (colEnd-colStart)//2>=1:
            # 좌상단
            devidePapers(rowStart, rowStart+(rowEnd-rowStart)//2, colStart, colStart+(colEnd-colStart)//2)
            # 우상단
            devidePapers(rowStart, rowStart+(rowEnd-rowStart)//2, colStart+(colEnd-colStart)//2, colEnd)
            # 우하단
            devidePapers(rowStart+(rowEnd-rowStart)//2, rowEnd, colStart+(colEnd-colStart)//2, colEnd)
            # 좌하단
            devidePapers(rowStart+(rowEnd-rowStart)//2, rowEnd, colStart, colStart+(colEnd-colStart)//2)

devidePapers(0, n, 0, n)
print(*colorPaper)
