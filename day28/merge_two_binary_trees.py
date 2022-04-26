# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1, root2):

        isRoot1Exist = root1 != None
        isRoot2Exist = root2 != None

        if isRoot1Exist == False and isRoot2Exist == False:
            return None

        sum_ = 0
        if root1 is not None:
            sum_ += root1.val
        if root2 is not None:
            sum_ += root2.val

        new_root = TreeNode(sum_)

        if isRoot1Exist and isRoot2Exist:
            new_root.left = self.mergeTrees(root1.left, root2.left)
            new_root.right = self.mergeTrees(root1.right, root2.right)
        elif isRoot1Exist and not isRoot2Exist:
            new_root.left = self.mergeTrees(root1.left, root2)
            new_root.right = self.mergeTrees(root1.right, root2)
        else:

            new_root.left = self.mergeTrees(root1, root2.left)
            new_root.right = self.mergeTrees(root1, root2.right)
        return new_root
