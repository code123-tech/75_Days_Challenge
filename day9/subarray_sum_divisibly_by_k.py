from collections import defaultdict


class Solution:
    def subarraysDivByK(self, nums, k):
        dicti = defaultdict(int)
        dicti[0] = 1
        sum_ = 0
        result = 0
        size = len(nums)
        for i in range(size):
            sum_ += nums[i]
            result += dicti[sum_ % k]
            dicti[sum_ % k] += 1
        return result


sol = Solution()
print(sol.subarraysDivByK([4, 5, 0, -2, -3, 1], 5))
