class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def findFloorCeil(root, key):
    floor, ceil = -1, -1
    while root:
        if root.value == key:
            floor = root.value
            ceil = root.value
        elif root.value > key:
            ceil = root.value
            root = root.left
        else:
            floor = root.value
            root = root.right

    print(key, floor, ceil)


root = Node(8)
root.left = Node(4)
root.right = Node(12)
root.left.left = Node(2)
root.left.right = Node(6)
root.right.left = Node(10)
root.right.right = Node(14)
for i in range(16):
    findFloorCeil(root, i)
