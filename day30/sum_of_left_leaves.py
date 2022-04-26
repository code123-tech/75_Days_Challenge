# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root) -> int:

        def dfs(node, dire, sum_):
            if node:
                if not node.left and not node.right:
                    if dire == 0:
                        sum_[0] += node.val
                dfs(node.left, 0, sum_)
                dfs(node.right, 1, sum_)
        sum_ = [0]
        dfs(root, 1, sum_)
        return sum_[0]
