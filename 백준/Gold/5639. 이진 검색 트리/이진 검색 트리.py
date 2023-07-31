import sys
sys.setrecursionlimit(10**9)

preorder= tuple(map(int, sys.stdin.readlines()))

def postorder(start, end):
    if start>end: return
    
    root = preorder[start]
    rightIdx = start + 1
    
    while rightIdx <= end:
        if preorder[rightIdx] > root: break
        rightIdx += 1

    postorder(start+1, rightIdx-1)
    postorder(rightIdx, end)
    print(preorder[start])
    
postorder(0, len(preorder)-1)