class Solution:
    def spiralOrder(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        if m == 1 and n == 1:
            return [matrix[0][0]]
        ans = [0]*(m*n)
        row_st, row_ed = 0, m-1
        col_st, col_ed = 0, n-1
        index = -1
        curr = 0
        while True:
            if curr >= (m*n):
                break
            # from top-left to top-right
            for col in range(col_st, col_ed+1):
                index += 1
                ans[index] = matrix[row_st][col]
                curr += 1
            row_st += 1
            if curr >= (m*n):
                break
            # from top-right to bottom-right
            for row in range(row_st, row_ed+1):
                index += 1
                ans[index] = matrix[row][col_ed]
                curr += 1
            col_ed -= 1
            if curr >= (m*n):
                break
            # from bottom-right to bottom left
            for col in range(col_ed, col_st-1, -1):
                index += 1
                ans[index] = matrix[row_ed][col]
                curr += 1
            row_ed -= 1
            if curr >= (m*n):
                break
            # from bottom-left to top-left
            for row in range(row_ed, row_st-1, -1):
                index += 1
                ans[index] = matrix[row][col_st]
                curr += 1
            col_st += 1
            if curr >= (m*n):
                break
        return ans


sol = Solution()
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(sol.spiralOrder(matrix))
