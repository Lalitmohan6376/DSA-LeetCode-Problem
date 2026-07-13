
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root,targetSum):
        if root is None:
            return False
        
        if root.left is None and root.right is None:
            return root.val == targetSum
            
        left = self.hasPathSum(root.left,targetSum-root.val)
        right = self.hasPathSum(root.right,targetSum-root.val)
        
        return left or right
        

root = TreeNode(5)

root.left = TreeNode(4)
root.right = TreeNode(8)

root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)

root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)

obj = Solution()

print(obj.hasPathSum(root, 22))  
print(obj.hasPathSum(root, 26))  
print(obj.hasPathSum(root, 18))
print(obj.hasPathSum(root, 20))
        
        
        
