class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def check(self, root):
        if root is None:
            return 0

        left = self.check(root.left)
        if left == -1:
            return -1

        right = self.check(root.right)
        if right == -1:
            return -1

        if abs(left - right) > 1:
            return -1

        return max(left, right) + 1

    def isBalanced(self, root):
        return self.check(root) != -1


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

obj = Solution()
print(obj.isBalanced(root))


# Brute Force Approach
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def height(self, root):
        if root is None:
            return 0
        
        left = self.height(root.left)
        right = self.height(root.right)
        
        return max(left,right) + 1
    
    def isBalanced(self,root):
        if root is None:
            return True
        
        left = self.height(root.left)
        right = self.height(root.right)

        if abs(left - right) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)
        
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

obj = Solution()
print(obj.isBalanced(root))
