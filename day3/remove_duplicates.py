class Solution:
    def removeDuplicates(self, nums):
        size = len(nums)
        if size == 0:
            return 0

        left = 0
        for right in range(1, size):
            if nums[right] != nums[left]:
                left += 1
                nums[left] = nums[right]

        return left + 1


sol = Solution()
print(sol.removeDuplicates([1, 1, 2]))
