class Solution:
    def pivotIndex(self, nums):
        size = len(nums)
        prefix = []
        result = -1
        prefix.append(0)
        for i in range(size):
            prefix.append(prefix[-1]+nums[i])
        right = 0

        for _ in range(len(nums)-1, -1, -1):
            if right == prefix[_]:
                result = _

            right += nums[_]
        return result


sol = Solution()
nums = [1, 7, 3, 6, 5, 6]
print(sol.pivotIndex(nums))
