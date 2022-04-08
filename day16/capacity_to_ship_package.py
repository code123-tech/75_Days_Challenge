class Solution:
    def shipWithinDays(self, weights, days: int) -> int:
        def isPossible(number):
            i = 0
            countDays = 0
            while i < len(weights):
                sum_ = 0
                j = i
                while i < len(weights) and sum_ <= number:
                    if weights[i] > number:
                        return False
                    sum_ += weights[i]
                    i += 1
                    if sum_ > number:
                        i -= 1
                        sum_ -= weights[i]
                        break
                if j == i:
                    i += 1
                countDays += 1
            return countDays <= days

        lower = 1
        higher = sum(weights)

        result = -1
        while lower <= higher:

            mid = (lower+higher)//2

            if isPossible(mid):
                result = mid
                higher = mid-1
            else:
                lower = mid+1
        return result


sol = Solution()
print(sol.shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
