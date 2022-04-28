# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root) -> int:
        q, maxi = deque([[root, 0]]), 0
        while len(q):
            maxi = max(maxi, q[-1][1] - q[0][1] + 1)
            for i in range(len(q)):
                node, pos = q.popleft()
                if node.left:
                    q.append([node.left, 2 * pos + 0])
                if node.right:
                    q.append([node.right, 2 * pos + 1])
        return maxi
