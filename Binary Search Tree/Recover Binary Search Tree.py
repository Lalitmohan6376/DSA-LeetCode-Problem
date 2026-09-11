# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverTree(self, root):
        first = None
        second = None
        previous = None

        def inorder(node):
            nonlocal first, second, previous

            if node is None:
                return

            inorder(node.left)

            if previous is not None and previous.val > node.val:
                if first is None:
                    first = previous
                second = node

            previous = node

            inorder(node.right)

        inorder(root)

        first.val, second.val = second.val, first.val
