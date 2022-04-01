class Solution:
    def canJump(self, nums):
        n = len(nums)
        back = n-1
        i = n-2
        while i >= 0:
            if i+nums[i] >= back:
                back = i
            i -= 1
        return back <= 0


sol = Solution()
print(sol.canJump([2, 3, 1, 1, 4]))
