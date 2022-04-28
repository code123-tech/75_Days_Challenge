# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def traverse(node):
            if node:
                traverse(node.left)
                traverse(node.right)
                temp = node.right
                node.right = node.left
                node.left = None
                while node.right != None:
                    node = node.right

                node.right = temp
        traverse(root)
