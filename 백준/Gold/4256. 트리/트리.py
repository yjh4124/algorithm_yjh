import sys

t=int(input())

for _ in range(t):
    n=int(input())

    preorder=[int(i) for i in sys.stdin.readline().split()]
    inorder=[int(i) for i in sys.stdin.readline().split()]

    # print(preorder)
    # print(inorder)


    def postorder(preorder, inorder):

        for idx in range(len(inorder)):
            if inorder[idx]==preorder[0]:
                div=idx
                break

        l_preorder=preorder[1:div+1]
        r_preorder=preorder[div+1:len(preorder)+1]
        l_inorder=inorder[:div]
        r_inorder=inorder[div+1:len(inorder)+1]
        
        if l_preorder!=[]:
            postorder(l_preorder, l_inorder)
        if r_preorder!=[]:    
            postorder(r_preorder, r_inorder)
        print(preorder[0],end=' ')

    postorder(preorder, inorder)
    print()