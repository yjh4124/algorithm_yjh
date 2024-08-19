# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
        
class Codec:
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result = []
        
        def dfs(node):
            if node is None:
                result.append("null")
                return
            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ','.join(result)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data_tokens=data.split(',')
        self.idx=0
        
        def make_tree():
            if data_tokens[self.idx]=="null":
                self.idx+=1
                return None
            
            node=TreeNode(int(data_tokens[self.idx]))
            self.idx+=1
            node.left=make_tree()
            node.right=make_tree()
            
            return node
            
        return make_tree()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))