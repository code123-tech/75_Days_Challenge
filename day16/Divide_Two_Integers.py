import math


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        x, y = math.modf(dividend/divisor)
        return int(y) if int(y) < (2**31-1) else 2**31-1


sol = Solution()
print(sol.divide(10, 3))
