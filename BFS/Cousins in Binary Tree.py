# Definition for a binary tree node.

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCousins(self, root,x,y):
        queue = deque([(root,None)])

        while queue:
            level = len(queue)
            x_parent = None
            y_parent = None

            for _ in range(level):
                node,parent = queue.popleft()

                if node.val == x:
                    x_parent = parent

                if node.val == y:
                    y_parent = parent

                if node.left:
                    queue.append((node.left,node))
                if node.right:
                    queue.append((node.right,node))

            if x_parent is not None or y_parent is not None:
                return x_parent is not None and y_parent is not None and x_parent != y_parent

        return False
