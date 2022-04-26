# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rec(self, root):
        if root is None:
            return 0
        return 1 + max(self.rec(root.left), self.rec(root.right))

    def maxDepth(self, root: TreeNode) -> int:
        return self.rec(root)
