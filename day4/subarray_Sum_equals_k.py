class Solution:
    def subarraySum(self, nums, k):
        if not nums:
            return 0

        dicti = {0: 1}
        rem = 0
        count = 0
        for i in range(len(nums)):
            rem += nums[i]

            if rem-k in dicti:
                count += dicti[rem-k]
            if rem in dicti:
                dicti[rem] += 1
            else:
                dicti[rem] = 1

        return count


sol = Solution()
print(sol.subarraySum([1, 1, 1], 2))
