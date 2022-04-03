import collections
import random


class RandomizedCollection:
    def __init__(self):
        self.vector = []  # Used For Storing Elements
        # used for storing index of each element
        self.hashTable = collections.defaultdict(set)

    def insert(self, val: int) -> bool:
        flag = True if self.hashTable[val] else False
        self.vector.append(val)
        self.hashTable[val].add(len(self.vector)-1)
        return not flag

    def remove(self, val: int) -> bool:
        flag = True if self.hashTable[val] else False
        if flag:
            # swaaping the val index with last element of the self.vector so that we can pop last element to reduce time complexiy to O(1).
            # Taking last inserted index of given val
            index = self.hashTable[val].pop()
            # removing val from last of the self.vector
            lastVal = self.vector[-1]
            # now replacing the last popped value with given value.
            self.vector[index] = lastVal
            self.hashTable[lastVal].add(index)
            self.hashTable[lastVal].discard(len(self.vector)-1)
            self.vector.pop()
            return flag
        else:
            return flag

    def getRandom(self) -> int:
        return random.choice(self.vector)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
