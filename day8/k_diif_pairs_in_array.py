from collections import defaultdict


class Solution:
    def findPairs(self, nums, k: int):
        dicti = defaultdict(int)

        for i in nums:
            dicti[i] += 1

        if k == 0:
            return sum([val > 1 for val in dicti.values()])

        return sum([1 for key in dicti if (key + k) in dicti])


sol = Solution()
nums = [3, 1, 4, 1, 5]
k = 2
print(sol.findPairs(nums, k))
