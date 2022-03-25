class Solution:
    def maxProfit(self, prices):
        if(len(prices) == 0):
            return 0

        minInd = 0
        maxInd = 0
        maxi = prices[0]
        lst = []

        for i in range(1, len(prices)):
            if(maxi < prices[i]):
                maxi = prices[i]
            elif(maxi > prices[i]):
                if(minInd != maxInd):
                    lst.append(abs(prices[maxInd]-prices[minInd]))
                minInd = i
                maxi = prices[i]
            elif(prices[minInd] == prices[i]):
                minInd = i
            maxInd = i

        if(minInd != maxInd):
            lst.append(prices[maxInd]-prices[minInd])

        return sum(lst)


sol = Solution()
prices = [7, 1, 5, 3, 6, 4]
print(sol.maxProfit(prices))
