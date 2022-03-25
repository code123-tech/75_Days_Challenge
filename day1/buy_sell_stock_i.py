class Solution:
    def maxProfit(self, A):
        profit = 0
        left = 0
        for right in range(1, len(A)):
            profit = max(profit, A[right]-A[left])
            if(A[right] < A[left]):
                left = right
        return profit


sol = Solution()
print(sol.maxProfit([7, 1, 5, 3, 6, 4]))
