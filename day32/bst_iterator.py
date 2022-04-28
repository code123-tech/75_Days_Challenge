class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def inorderLeft(self, root, lst):
        if root is None:
            return
        lst.append(root)
        self.inorderLeft(root.left, lst)

    def __init__(self, root):
        self.lst = []
        self.inorderLeft(root, self.lst)

    def next(self) -> int:
        node = self.lst.pop()
        self.inorderLeft(node.right, self.lst)
        return node.val

    def hasNext(self) -> bool:
        return len(self.lst) != 0
