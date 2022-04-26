# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.res = 0

        def sol_rec(cur, val):
            if cur.val >= val:
                self.res += 1
            if cur.left:
                sol_rec(cur.left, max(val, cur.val))
            if cur.right:
                sol_rec(cur.right, max(val, cur.val))

        sol_rec(root, root.val)
        return self.res
