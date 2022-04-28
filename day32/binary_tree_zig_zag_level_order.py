# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root):
        if root is None:
            return []

        result = []
        index = 0
        queue = deque()
        queue.append(root)
        while queue:
            temp = []
            for i in range(len(queue)):
                node = queue.popleft()
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if index & 1:
                result.append(temp[::-1])
            else:
                result.append(temp)
            index = 1 - index
        return result
