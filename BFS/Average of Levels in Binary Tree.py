from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root):
        if root is None:
            return []

        queue = deque([root])
        ans = []

        while queue:
            total = 0
            count = len(queue)

            for _ in range(count):
                node = queue.popleft()

                total += node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            avg = total / count
            ans.append(avg)

        return ans
