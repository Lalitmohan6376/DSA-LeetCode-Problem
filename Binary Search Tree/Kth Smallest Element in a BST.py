# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
      
class Solution:
    def kthSmallest(self, root, k):
      self.ans = []

      def inorder(node):
        inorder(node.left)
        self.ans.append(root.val)
        inorder(node.right)
        
      inorder(root)

      element = self.ans[k - 1]

      return element
