import sys

n = int(input())

tree = {}

# print(ls)

def preorder(tree,node):

    for data in tree.items():
        
        if data[0]==node:
            print(node,end='')
            if data[1][0]!='.':
                preorder(tree, data[1][0])
            if data[1][1]!='.':
                preorder(tree, data[1][1])


def inorder(tree,node):
    for data in tree.items():
        
        if data[0]==node:
            if data[1][0]!='.':
                inorder(tree, data[1][0])
            print(node,end='')
            if data[1][1]!='.':
                inorder(tree, data[1][1])

def postorder(tree,node):
    for data in tree.items():
        
        if data[0]==node:
            if data[1][0]!='.':
                postorder(tree, data[1][0])
            if data[1][1]!='.':
                postorder(tree, data[1][1])
            print(node,end='')

for i in range(n):

    node, left, right = [i for i in sys.stdin.readline().split()]

    tree[node]=[left, right]

preorder(tree, list(tree.keys())[0])
print('')
inorder(tree, list(tree.keys())[0])
print('')
postorder(tree, list(tree.keys())[0])