class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def isSameTree(self, root, subRoot):
        if root is None and subRoot is None:
            return True

        if root is None or subRoot is None:
            return False

        if root.val != subRoot.val:
            return False

        return (self.isSameTree(root.left, subRoot.left) and
                self.isSameTree(root.right, subRoot.right))

    def isSubtree(self, root, subRoot):

        if root is None:
            return False

        if self.isSameTree(root, subRoot):
            return True

        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right,subRoot))

root = TreeNode(3)

root.left = TreeNode(4)

root.right = TreeNode(5)

root.left.left = TreeNode(1)

root.left.right = TreeNode(2)

subRoot = TreeNode(4)

subRoot.left = TreeNode(1)

subRoot.right = TreeNode(2)

obj = Solution()

print(obj.isSubtree(root,subRoot))
