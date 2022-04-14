class Solution:
    def sortedSquares(self, nums):
        result = []
        left = 0
        right = len(nums)-1
        while left <= right:
            if abs(nums[left]) < abs(nums[right]):
                result.append(nums[right]**2)
                right -= 1
            else:
                result.append(nums[left]**2)
                left += 1
        return result[::-1]


sol = Solution()
nums = [-4, -1, 0, 3, 10]
print(sol.sortedSquares(nums))
