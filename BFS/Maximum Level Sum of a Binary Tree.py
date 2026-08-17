# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxLevelSum(self, root):
        maxsum = 0
        anslevel = 0
        level = 1
        queue = deque([root])
        while queue:
            sum = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                sum+=node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if sum > maxsum:
                maxsum = sum
                anslevel = level
            level+=1
        return anslevel 
