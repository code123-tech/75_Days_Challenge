class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def search(self, value):
        if self.root == None:
            return False
        else:
            return self._search(value, self.root)

    def insert(self, value):
        if self.root == None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value <= cur_node.value:
            if cur_node.left == None:
                cur_node.left = Node(value)
            else:
                self._insert(value, cur_node.left)
        elif value > cur_node.value:
            if cur_node.right == None:
                cur_node.right = Node(value)
            else:
                self._insert(value, cur_node.right)

    def _search(self, value, cur_node):
        if value == cur_node.value:
            return True
        elif value < cur_node.value and cur_node.left != None:
            return self._search(value, cur_node.left)
        elif value > cur_node.value and cur_node.right != None:
            return self._search(value, cur_node.right)
        return False

    def _inorder(self, cur_node):
        if cur_node != None:
            self._inorder(cur_node.left)
            print(cur_node.value)
            self._inorder(cur_node.right)

    def inorder(self):
        if self.root != None:
            self._inorder(self.root)

    def get_min(self, cur_node):
        if cur_node.left == None:
            return cur_node
        else:
            return self.get_min(cur_node.left)

    def _delete(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left != None:
                self._delete(value, cur_node.left)
        elif value > cur_node.value:
            if cur_node.right != None:
                self._delete(value, cur_node.right)
        else:
            if cur_node.left == None and cur_node.right == None:
                cur_node = None
            elif cur_node.left == None:
                cur_node = cur_node.right
            elif cur_node.right == None:
                cur_node = cur_node.left
            else:
                del_node = self.get_min(cur_node.right)
                cur_node.value = del_node.value
                self._delete(del_node.value, cur_node.right)

    def delete(self, value):
        if self.root != None:
            self._delete(value, self.root)


bst = BST()
bst.insert(9)
bst.insert(4)
bst.insert(6)
bst.insert(20)
bst.insert(170)
bst.inorder()
bst.delete(4)
bst.inorder()
