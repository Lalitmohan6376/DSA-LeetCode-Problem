# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestZigZag(self, root):
        def dfs(node,direction,length):
            if node is None:
                return length-1
                
            if direction == "left":
                left = dfs(node.left,"right",length+1)
                right = dfs(node.right,"left",1)
            else:
                right = dfs(node.right,"left",length+1)
                left = dfs(node.left,"right",1)
            return max(left,right)
            
        return max(dfs(root.left, "right",1),
        dfs(root.right,"left",1)
        )
                
        
