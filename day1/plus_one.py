class Solution:
    def plusOne(self, digits):
        power = 0
        n = len(digits)

        for i in range(n-1, -1, -1):
            num = digits[i] + power
            num = num + (1 if i == n - 1 else 0)
            power, digits[i] = divmod(num, 10)
            if power == 0:
                break
        if power > 0:
            digits = [power] + digits

        return digits


sol = Solution()
print(sol.plusOne([1, 2, 3]))
