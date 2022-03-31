class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts, verticalCuts):
        horizontalCuts = [0] + horizontalCuts + [h]
        verticalCuts = [0] + verticalCuts + [w]
        mod = 10**9+7
        horizontalCuts.sort()
        verticalCuts.sort()

        horizontalMax = float("-inf")
        for i in range(len(horizontalCuts)-1):
            diff = horizontalCuts[i+1]-horizontalCuts[i]
            horizontalMax = max(horizontalMax, diff)

        verticalMax = float("-inf")
        for i in range(len(verticalCuts)-1):
            diff = verticalCuts[i+1]-verticalCuts[i]
            verticalMax = max(verticalMax, diff)

        return (horizontalMax*verticalMax) % mod


sol = Solution()
h = 10
w = 10
horizontalCuts = [1, 2, 5, 6]
verticalCuts = [3, 4]
print(sol.maxArea(h, w, horizontalCuts, verticalCuts))
