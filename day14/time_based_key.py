import collections


class TimeMap:

    def __init__(self):
        self.dicti = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:

        self.dicti[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:

        lst = self.dicti[key]

        left = 0
        right = len(lst)
        while left < right:
            mid = (left+right)//2
            if lst[mid][1] <= timestamp:
                left = mid+1
            else:
                right = mid
        return "" if right == 0 else lst[right-1][0]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
