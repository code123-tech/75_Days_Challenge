class Solution:

    def searchEl(self, low, high, nums, target, bisect_left=True):
        pos = -1
        while low <= high:
            mid = low + (high-low)//2
            if nums[mid] == target:
                pos = mid
                if bisect_left:
                    high = mid-1
                else:
                    low = mid+1
            elif nums[mid] > target:
                high = mid-1
            else:
                low = mid+1
        return pos

    def searchRange(self, nums, target: int):

        if not nums:
            return [-1, -1]

        return [self.searchEl(0, len(nums)-1, nums, target), self.searchEl(0, len(nums)-1, nums, target, False)]


sol = Solution()
print(sol.searchRange([5, 7, 7, 8, 8, 10], 8))
