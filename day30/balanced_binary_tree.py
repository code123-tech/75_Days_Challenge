# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.ans = True

        def dfs(node):
            if not node or not self.ans:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if abs(left-right) > 1:
                self.ans = False
                return 0
            return max(left, right)+1
        self.ans = True
        dfs(root)
        return self.ans
