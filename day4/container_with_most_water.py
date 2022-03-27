class Solution:
    def maxArea(self, height):
        maxi = 0
        left = 0
        right = len(height)-1
        while left < right:
            if height[left] < height[right]:
                maxi = max(maxi, height[left]*(right-left))
                left += 1
            else:
                maxi = max(maxi, height[right]*(right-left))
                right -= 1
        return maxi


sol = Solution()
print(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
