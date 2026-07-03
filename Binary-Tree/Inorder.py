# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
       self.ans = []

    def Inorder(self,root):
      # Base case
      if root is None:
        return
      
      
      self.Inorder(root.left)
      self.ans.append(root.val)
      self.Inorder(root.right)

    def inorderTraversal(self, root):
      self.ans = []
      self.Inorder(root)
      return self.ans
    
        
