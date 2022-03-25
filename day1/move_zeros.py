class Solution:
    def moveZeroes(self, nums):
        size = len(nums)
        last = 0
        for i in range(size):
            if nums[i] != 0:
                nums[i], nums[last] = nums[last], nums[i]
                last += 1


sol = Solution()
nums = [0, 1, 0, 3, 12]
sol.moveZeroes(nums)
