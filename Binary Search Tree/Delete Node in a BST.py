# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root, key):

        values = []

        def inorder(node):
            if node is None:
                return

            inorder(node.left)

            if node.val != key:
                values.append(node.val)

            inorder(node.right)

        inorder(root)

        def buildTree(left, right):
            if left > right:
                return None

            middle = (left + right) // 2

            node = TreeNode(values[middle])

            node.left = buildTree(left, middle - 1)
            node.right = buildTree(middle + 1, right)

            return node

        return buildTree(0, len(values) - 1)

#optimal solution

class Solution:
    def deleteNode(self, root, key):

        if root is None:
            return None

        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:

            if root.left is None and root.right is None:
                return None

    
            if root.left is None:
                return root.right

            if root.right is None:
                return root.left

            current = root.right

            while current.left is not None:
                current = current.left

            root.val = current.val

            root.right = self.deleteNode(root.right, current.val)

        return root
