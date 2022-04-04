class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        total0, total1, total2 = 0, 0, 0
        for i in nums:
            if i == 0:
                total0 += 1
            elif i == 1:
                total1 += 1
            else:
                total2 += 1
        for i in range(total0):
            nums[i] = 0
        for _ in range(total0, total1+total0):
            nums[_] = 1
        for _ in range(total1+total0, total1+total0+total2):
            nums[_] = 2


sol = Solution()
nums = [2, 0, 2, 1, 1, 0]
sol.sortColors(nums)
print(nums)
