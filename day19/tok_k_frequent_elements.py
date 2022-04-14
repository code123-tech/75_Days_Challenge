from collections import Counter


class Solution:
    def topKFrequent(self, nums, k: int):
        most_common = Counter(nums).most_common()
        fin = []
        for l in range(0, k):
            fin.append(most_common[l][0])

        return fin


sol = Solution()
print(sol.topKFrequent([1, 1, 1, 2, 2, 3], 2))
