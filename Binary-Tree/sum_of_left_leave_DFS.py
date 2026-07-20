# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root,isleft=False):
        if root is None:
            return 0
        
        if root.left is None and root.right is None:
            if isleft:
                return root.val
            else:
                return 0
            
        left = self.sumOfLeftLeaves(root.left,True)
        right = self.sumOfLeftLeaves(root.right,False)

        return left + right

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

obj = Solution()
print(obj.sumOfLeftLeaves(root))
