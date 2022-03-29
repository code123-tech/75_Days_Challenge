class Solution:
    def __init__(self):
        self.rowl = [0, 0, 1, -1, -1, 1, -1, 1]
        self.coll = [-1, 1, 0, 0, -1, 1, 1, -1]

    def check(self, i, j, row, col):
        if i >= 0 and j >= 0 and i < row and j < col:
            return True
        return False

    def check1(self, i, j, row, col, board):
        noOfzero = 0
        for k in range(8):
            if self.check(i+self.rowl[k], j+self.coll[k], row, col):
                if board[i+self.rowl[k]][j+self.coll[k]][0] == 1:
                    noOfzero += 1
        return noOfzero

    def gameOfLife(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        row = len(board)
        col = len(board[0])
        for i in range(row):
            for j in range(col):
                board[i][j] = [board[i][j]]

        for i in range(row):
            for j in range(col):
                # check for live cell
                if board[i][j][0] == 1:
                    # first condition
                    noOfone = self.check1(i, j, row, col, board)
                    if noOfone < 2 or noOfone > 3:
                        board[i][j].append(0)
                    else:
                        board[i][j].append(1)
                else:
                    noOfone = self.check1(i, j, row, col, board)
                    if noOfone == 3:
                        board[i][j].append(1)
                    else:
                        board[i][j].append(0)
        for i in range(row):
            for j in range(col):
                board[i][j] = board[i][j][1]


sol = Solution()
board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
sol.gameOfLife(board)
print(board)
