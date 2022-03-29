import collections


class Solution:
    def numPairsDivisibleBy60(self, time):
        remainders = collections.defaultdict(int)
        ret = 0
        for t in time:
            ret += remainders[(60-t) % 60]
            remainders[t % 60] += 1
        return ret


sol = Solution()
time = [30, 20, 150, 100, 40]
print(sol.numPairsDivisibleBy60(time))
