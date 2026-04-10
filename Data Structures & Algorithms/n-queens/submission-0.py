class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for _ in range(n)] for _ in range(n)]
        res = []
        print(board)
        def is_valid(board, r, c):
            for i in range(c):
                if board[r][i] == "Q":
                    return False
            for i, j  in zip(range(r, -1, -1), range(c, -1, -1)):
                if board[i][j] == "Q":
                    return False
            for i, j in zip(range(r,n), range(c, -1, -1)):
                if board[i][j] == "Q":
                    return False
            return True

        def backtrack(board, col):
            if col >= n:
                res.append(["".join(row) for row in board])
                print(res)

            for row in range(n):
                # print(row, col)
                if is_valid(board, row, col):
                    board[row][col] = "Q"
                    backtrack(board, col + 1)
                    board[row][col] = "."

        backtrack(board, 0)
        return res