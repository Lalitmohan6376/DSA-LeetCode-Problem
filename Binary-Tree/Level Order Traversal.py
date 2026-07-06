
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root):
        if root == None:
            return []
        
        qu = []
        ans = []

        qu.append(root)
        
        while qu:
            size = len(qu)
            level = []

            for i in range(size):
                node = node = qu.pop(0)
                level.append(node.val)

                if node.left:
                    qu.append(node.left)
                if node.right:
                    qu.append(node.right)
            ans.append(level)
        return ans
    
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

obj = Solution()
print(obj.levelOrder(root))
