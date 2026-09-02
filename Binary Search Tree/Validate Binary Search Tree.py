# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
       
class Solution:
    def isValidBST(self, root):

        def check(node, low, high):
            if node is None:
                return True

            if node.val <= low or node.val >= high:
                return False

            left = check(node.left, low, node.val)

            if left == False:
                return False

            right = check(node.right, node.val, high)

            if right == False:
                return False

            return True

        return check(root, float("-inf"), float("inf"))
