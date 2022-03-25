from sortedcontainers import SortedList


class Solution:
    def sortedSquares(self, nums):
        return SortedList([x*x for x in nums])


sol = Solution()
nums = [-4, -1, 0, 3, 10]
print(sol.sortedSquares(nums))
