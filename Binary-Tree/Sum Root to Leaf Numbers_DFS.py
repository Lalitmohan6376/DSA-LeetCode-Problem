# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root):
        def dfs(node,current):
            if node is None:
                return 0
            
            current = current * 10 + node.val
            
            if node.left is None and node.right is None:
                return current
                
            left = dfs(node.left,current)
            right = dfs(node.right,current)
            
            return left + right
        
        return dfs(root,0)
                
            
        
