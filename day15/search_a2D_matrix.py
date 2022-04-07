class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        row = 0
        col = len(matrix[0])-1

        while row < rows and col >= 0:

            if matrix[row][col] == target:
                return True
            if matrix[row][col] > target:
                col -= 1
            else:
                row += 1

        return False


sol = Solution()
print(sol.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 3))
