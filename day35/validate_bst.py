# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def check(self, node, mini=-2147483649, maxi=2147483648):
        if node is None:
            return True
        if node.val <= mini or node.val >= maxi:
            return False
        left = self.check(node.left, mini, node.val)
        right = left and self.check(node.right, node.val, maxi)
        return right

    def isValidBST(self, root: TreeNode) -> bool:
        return self.check(root)
