class DoublyLinkedList:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = dict()
        self.head = DoublyLinkedList(0, 0)
        self.tail = DoublyLinkedList(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.hashmap:
            node = self.hashmap[key]
            self.removeNode(node)
            self.add_node_at_the_end(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.removeNode(self.hashmap[key])
        node = DoublyLinkedList(key, value)
        self.add_node_at_the_end(node)
        self.hashmap[key] = node
        if len(self.hashmap) > self.capacity:
            removeNode = self.head.next
            self.removeNode(removeNode)
            del self.hashmap[removeNode.key]

    def removeNode(self, node):
        prev = node.prev
        nexti = node.next
        prev.next = nexti
        nexti.prev = prev

    def add_node_at_the_end(self, node):
        prev = self.tail.prev
        prev.next = node
        self.tail.prev = node
        node.next = self.tail
        node.prev = prev


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
