# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructFromPrePost(self, preorder, postorder):
        size = len(preorder)

        dicti = {}
        for i in range(size):
            dicti[postorder[i]] = i

        def getTreeNode(pre_st_ind, pre_end_ind, post_st_ind, post_end_ind):
            if pre_st_ind > pre_end_ind:
                return None

            root = TreeNode(preorder[pre_st_ind])
            if pre_st_ind == pre_end_ind:
                return root
            index = dicti[preorder[pre_st_ind+1]]

            total = index - post_st_ind + 1

            root.left = getTreeNode(
                pre_st_ind+1, pre_st_ind + total, post_st_ind, index)
            root.right = getTreeNode(
                pre_st_ind + total + 1, pre_end_ind, index+1, post_end_ind)

            return root

        return getTreeNode(0, size-1, 0, size-1)
