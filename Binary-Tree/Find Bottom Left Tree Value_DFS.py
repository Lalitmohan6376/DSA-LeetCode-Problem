# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findBottomLeftValue(self, root):
        def dfs(node):
            if node is None:
                return (0, None)

            left_height,left_value = dfs(node.left)
            right_height,right_value = dfs(node.right)

            if left_height == 0 and right_height == 0:
                return (1,node.val)

            if left_height >= right_height:
                return (left_height + 1, left_value)
            else:
                return (right_height + 1, right_value)
        return dfs(root)[1]

        

        
