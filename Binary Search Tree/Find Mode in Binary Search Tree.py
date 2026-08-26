class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root):
        self.freq = {}

        def inorder(node):
            if node is None:
                return

            inorder(node.left)

            self.freq[node.val] = self.freq.get(node.val, 0) + 1

            inorder(node.right)

        inorder(root)

    
        max_freq = 0

        for value in self.freq:
            if self.freq[value] > max_freq:
                max_freq = self.freq[value]


        ans = []

        for value in self.freq:
            if self.freq[value] == max_freq:
                ans.append(value)

        return ans
