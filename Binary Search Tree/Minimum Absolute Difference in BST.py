# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root):
        self.prev = None
        self.min_diff = float('inf')

        def inorder(node):
            if node is None:
                return

            inorder(node.left)

            if self.prev is not None:
                diff = node.val - self.prev

                if diff < self.min_diff:
                    self.min_diff = diff

            self.prev = node.val

            inorder(node.right)

        inorder(root)

        return self.min_diff
