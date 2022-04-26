# Definition for a binary tree node.
import copy


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findPath(self, root, lst, temp):
        if(root is None):
            return
        if(root.left is None and root.right is None):
            temp.append(str(root.val))
            lst.append("->".join(copy.deepcopy(temp)))
            temp.pop()
            return
        temp.append(str(root.val))
        self.findPath(root.left, lst, temp)
        self.findPath(root.right, lst, temp)
        temp.pop()

    def binaryTreePaths(self, root: TreeNode):
        lst = []
        temp = []
        self.findPath(root, lst, temp)
        return lst
