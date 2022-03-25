from collections import defaultdict


class Solution:
    def twoSum(self, nums, target):
        dicti = defaultdict(list)
        n = len(nums)

        for i in range(n):
            dicti[nums[i]].append(i)

        for i in range(len(nums)):
            tempTarget = target - nums[i]
            if tempTarget in dicti:
                for j in dicti[tempTarget]:
                    if i != j:
                        return [i, j]


sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))
