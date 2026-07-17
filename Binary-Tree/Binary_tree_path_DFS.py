# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root):
        ans = []

        def dfs(root,path):
            if root is None:
                return
            
            if path == "":
                path = str(root.val)
            else:
                path = path + "->" + str(root.val)

            if root.left is None and root.right is None:
                ans.append(path)
                return
            
            dfs(root.left,path)
            dfs(root.right,path)

        dfs(root,"")
        return ans
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

root.left.right = TreeNode(5)

obj = Solution()
print(obj.binaryTreePaths(root))
