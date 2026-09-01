# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def increasingBST(self, root):

        values = []

        def inorder(node):
            if node is None:
                return

            inorder(node.left)

            values.append(node.val)

            inorder(node.right)

        inorder(root)

        new_root = TreeNode(values[0])
        current = new_root

        for i in range(1, len(values)):
            current.right = TreeNode(values[i])
            current = current.right

        return new_root




# 2 Solution:

class Solution:
    def increasingBST(self, root):

        dummy = TreeNode(0)
        prev = dummy

        def inorder(node):
            nonlocal prev

            if node is None:
                return

            inorder(node.left)

            node.left = None
            prev.right = node
            prev = node

            inorder(node.right)

        inorder(root)

        return dummy.right
