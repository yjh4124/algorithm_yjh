# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        subtrees ={}
        duplicates = []
        def serialize(node):
            if not node:
                return ''
            left = serialize(node.left)
            right = serialize(node.right)

            subtree = "{},{},{}".format(node.val,left,right)
            subtrees[subtree] = subtrees.get(subtree, 0) + 1

            if subtrees[subtree] == 2:
                duplicates.append(node)
            return subtree
        serialize(root)
        return duplicates  
    
#         memo_paths=[]
        
#         def bfs(root):
#             queue=deque([(root, [])])
            
#             while queue:
#                 node, path=queue.popleft()
#                 node_l=node.left
#                 node_r=node.right
#                 if node_l is None and node_r is None:
#                     memo_paths.append(path)
#                     continue
#                 if node_l is not None: queue.append((node_l, path+["{}_l".format(node_l.val)]))
#                 if node_r is not None: queue.append((node_r, path+["{}_r".format(node_r.val)]))
        
#         def find_duplicate_structures(memo_paths):
#             memo_token_paths={}
#             duplicates = []
            
#             for path in memo_paths:
#                 while path:
#                     path[0]=path[0][0]+'_root'
#                     memo_token_paths[' '.join(path)]=memo_token_paths.get(' '.join(path), 0)+1
#                     path.pop(0)
            
#             for key, value in memo_token_paths.items():
#                 if value>=2: duplicates.append(key)
                    
#             return duplicates
        
#         def make_trees(structures):
#             trees=[]
#             for structure in structures:
#                 for idx, elem in enumerate(structure.split()):
#                     val, position=elem.split('_')
#                     if idx==0: 
#                         tree=TreeNode(int(val))
#                         node=tree
#                         continue
#                     if position=='l':
#                         node.left=TreeNode(int(val))
#                         node=node.left
#                     else:
#                         node.right=TreeNode(int(val))
#                         node=node.right
                
#                 trees.append(tree)
                
#             return trees
        
#         bfs(root)
#         same_structures=find_duplicate_structures(memo_paths)
#         return make_trees(same_structures)
    
    