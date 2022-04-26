# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        self.result = None
        if p.val > q.val:
            temp = p
            p = q
            q = temp

        def recursion(node):
            if node is None:
                return None

            if node.val >= p.val and node.val <= q.val:
                self.result = node
                return

            if p.val < node.val and q.val < node.val:
                recursion(node.left)
            else:
                recursion(node.right)
        recursion(root)
        return self.result
