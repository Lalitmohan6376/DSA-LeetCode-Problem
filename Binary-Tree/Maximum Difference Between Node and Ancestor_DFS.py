# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxAncestorDiff(self, root):
        ans = 0
        
        def dfs(node,minimum,maximum):
            nonlocal ans
            
            if node is None:
                return
            
            diff1 = abs(node.val - minimum)
            diff2 = abs(node.val - maximum)
            
            ans = max(ans,diff1,diff2)
            
            minimum = min(minimum,node.val)
            maximum = max(maximum,node.val)
            
            dfs(node.left,minimum,maximum)
            dfs(node.right,minimum,maximum)
            
        dfs(root,root.val,root.val)
        return ans
        
