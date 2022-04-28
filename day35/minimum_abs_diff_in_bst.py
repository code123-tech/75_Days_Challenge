# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, root):
        if root:
            l_min, l_abs, l_max = self.dfs(root.left)
            r_min, r_abs, r_max = self.dfs(root.right)
            return min(l_min, root.val), min(l_abs, r_abs, root.val-l_max, r_min-root.val), max(r_max, root.val)
        return float("inf"), float("inf"), float("-inf")

    def getMinimumDifference(self, root: TreeNode) -> int:
        min, abs, max = self.dfs(root)
        return abs
