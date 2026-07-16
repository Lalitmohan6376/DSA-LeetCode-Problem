class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mirror(self,left,right):
        if left is None and right is None:
            return True

        if left is None or right is None:
            return False

        if left.val != right.val:
            return False

        leftans = self.mirror(left.left,right.right)
        rightans = self.mirror(left.right,right.left)

        return leftans and rightans

    def isSymmetric(self,root):
        if root is None:
            return True
        
        return self.mirror(root.left,root.right)
    

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

obj = Solution()
print(obj.isSymmetric(root))
