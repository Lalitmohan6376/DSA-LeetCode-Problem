# Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def findTarget(self, root,k):
      values = []

      def inorder(node):
        if node is None:
          return

        inorder(node.left)
        values.append(node.val)
        inorder(node.right)
      inorder(root)

      left = 0
      right = len(values)-1

      while left < right:
        total = values[left] + values[right]
        if total == k:
          return True
        if total < k:
          left+=1
        else:
          right-=1
      return False

    
