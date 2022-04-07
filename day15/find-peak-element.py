class Solution:
    def findPeakElement(self, nums) -> int:
        left = 0
        right = len(nums)-1
        while left < right:
            mid = left + (right-left)//2
            if nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid+1
        return left


sol = Solution()
print(sol.findPeakElement([1, 2, 3, 1]))
