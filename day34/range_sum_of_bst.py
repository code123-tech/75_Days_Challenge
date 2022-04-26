# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root:
            return 0
        self.sum = 0

        def traverse(node):
            if(node.val >= low and node.val <= high):
                self.sum += node.val
            if(node.val > low and node.left):
                traverse(node.left)
            if(node.val < high and node.right):
                traverse(node.right)
        traverse(root)
        return self.sum
