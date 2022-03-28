class Solution:
    def exist(self, board, word):

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def dfs(i, j, w):
            if len(w) == 0:
                return True
            if i < 0 or i >= row or j < 0 or j >= col or board[i][j] != w[0]:
                return False

            char = board[i][j]
            board[i][j] = "#"

            for ii, jj in directions:
                nextI, nextJ = i + ii, j+jj
                if dfs(nextI, nextJ, w[1:]):
                    return True
            board[i][j] = char
            return False

        row = len(board)
        col = len(board[0])
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0] and dfs(i, j, word):
                    return True
        return False


sol = Solution()
board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]
print(sol.exist(board, "ABCCED"))
