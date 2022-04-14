class MyHashMap:

    def calculate(self, key):
        return ((key*1098999) & (1 << 20)-1) >> 5

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mapi = [[] for i in range(1 << 15)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hash = self.calculate(key)

        for i, (key1, value1) in enumerate(self.mapi[hash]):
            if key == key1:
                self.mapi[hash][i] = (key, value)
                return
        self.mapi[hash].append((key, value))

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hash = self.calculate(key)

        for i, (key1, value) in enumerate(self.mapi[hash]):
            if key == key1:
                return value
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hash = self.calculate(key)

        for i, (key1, value) in enumerate(self.mapi[hash]):
            if key == key1:
                self.mapi[hash].remove((key, value))
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
