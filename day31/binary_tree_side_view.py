# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: TreeNode):
        if(root is None):
            return []
        q = collections.deque()
        ans = [root.val]
        if(root.left):
            q.append(root.left)
        if(root.right):
            q.append(root.right)
        while q:
            size = len(q)
            for i in range(size):
                temp = q.popleft()
                if(i == size-1):
                    ans.append(temp.val)
                if(temp.left):
                    q.append(temp.left)
                if(temp.right):
                    q.append(temp.right)
        return ans
