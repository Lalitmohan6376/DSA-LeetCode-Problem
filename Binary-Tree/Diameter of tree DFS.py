# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.diameter = 0
    
    def height(self,root):
        if root is None:
            return 0
        
        left = self.height(root.left)
        right = self.height(root.right)

        self.diameter = max(self.diameter,left + right)

        return max(left,right) + 1
    
    def diameterOfBinaryTree(self, root):
        self.height(root)
        return self.diameter
