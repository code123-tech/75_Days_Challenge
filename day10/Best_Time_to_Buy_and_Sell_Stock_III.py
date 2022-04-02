class Solution:
    def maxProfit(prices):
        size = len(prices)
        left = [0]*size
        right = [0]*size
        left_min_price = prices[0]
        right_max_price = prices[size-1]

        for i in range(1, size):
            left[i] = max(left[i-1], prices[i]-left_min_price)
            left_min_price = min(left_min_price, prices[i])

        for i in range(size-2, -1, -1):
            right[i] = max(right[i+1], right_max_price-prices[i])
            right_max_price = max(right_max_price, prices[i])

        max_profit = 0
        for i in range(size):
            max_profit = max(max_profit, left[i]+right[i])
        return max_profit


sol = Solution()
prices = [3, 3, 5, 0, 0, 3, 1, 4]
print(sol.maxProfit(prices))


'''
3   3    5   0   0   3   1   4
  |    | - |   |   |   |   |
  |    | - |   |   |   |   | -
- | -  | - |   |   | - |   | -   
- | -  | - |   |   | - |   | -
- | -  | - | * | * | - | - | -
0 | 1  | 2 | 3 | 4 | 5 | 6 | 7  


left = [0, 0, 2, 2, 2, 3, 3, 4]

right = [4, 4, 4, 4, 4, 3, 3, 0]



'''
