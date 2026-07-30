# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def delNodes(self, root, to_delete):
        delete = set(to_delete)
        ans = []
        
        def dfs(node,is_root):
            if node is None:
                return None
                
            deleted = node.val in delete
            
            if is_root and not deleted:
                ans.append(node)
                
            node.left = dfs(node.left,deleted)
            node.right = dfs(node.right,deleted)
            
            if deleted:
                return None
            return node
        dfs(root,True)
        return ans
        
