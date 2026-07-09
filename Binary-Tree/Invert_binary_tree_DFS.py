class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root):
        if root is None:
            return

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right
        root.right = left
        return root


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)

root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

obj = Solution()
new_root = obj.invertTree(root)

def preorder(root):
    if root is None:
        return
    
    print(root.val,end=" ")
    preorder(root.left)
    preorder(root.right)

preorder(root)

