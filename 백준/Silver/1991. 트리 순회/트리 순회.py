n=int(input())
trees={}

def getDict(trees):
    for _ in range(n):
        parent, left, right=input().split()
        trees[parent]=[left, right]
    return trees

trees=getDict(trees)

def preorder(root):
    if root!='.': print(root,end='')
    if trees[root][0]!='.': preorder(trees[root][0])
    if trees[root][1]!='.': preorder(trees[root][1])

def inorder(root):
    if trees[root][0]!='.': inorder(trees[root][0])
    if root!='.': print(root,end='')
    if trees[root][1]!='.': inorder(trees[root][1])

def postorder(root):
    if trees[root][0]!='.': postorder(trees[root][0])
    if trees[root][1]!='.': postorder(trees[root][1])
    if root!='.': print(root,end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')