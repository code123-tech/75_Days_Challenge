import random


class RandomizedSet:

    def __init__(self):
        self.hashTable = {}  # used for storing index of each element

    def insert(self, val: int) -> bool:
        if val in self.hashTable:
            return False
        self.hashTable[val] = 1
        return True

    def remove(self, val: int) -> bool:
        if val in self.hashTable:
            self.hashTable.pop(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(list(self.hashTable.keys()))


ran = RandomizedSet()
