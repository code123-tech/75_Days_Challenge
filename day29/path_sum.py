# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        self.ans = False

        def recur(node, tempSum):
            if node is None:
                return 0

            if node.left == None and node.right == None:
                tempSum += node.val
                if tempSum == targetSum:
                    tempSum -= node.val
                    self.ans = True
                    return
            else:
                tempSum += node.val

            recur(node.left, tempSum)
            recur(node.right, tempSum)

        recur(root, 0)
        return self.ans
