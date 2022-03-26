class Solution:
    def generate(self, numRows):
        result = []

        for i in range(numRows):
            if i == 0:
                result.append([1])
            else:
                prevRow = result[-1]
                newRow = [prevRow[j]+prevRow[j+1]
                          for j in range(len(prevRow)-1)]
                newRow = [1] + newRow + [1]
                result.append(newRow)
        return result


sol = Solution()
print(sol.generate(5))
