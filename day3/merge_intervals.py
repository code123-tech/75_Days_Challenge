class Solution:
    def merge(self, intervals):

        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]
        for lst in intervals[1:]:
            if result[-1][-1] < lst[0]:
                result.append(lst)
            else:
                result[-1][-1] = max(result[-1][-1], lst[-1])
        return result


sol = Solution()
print(sol.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
