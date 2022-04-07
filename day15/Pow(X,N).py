class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
        n = abs(n)
        if n == 0:
            return 1
        temp = self.myPow(x, n >> 1)
        if n & 1:
            return x*temp*temp
        return temp*temp


sol = Solution()
print(sol.myPow(2.00000, 10))
