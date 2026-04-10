class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m = 9

        row = [set() for _ in range(m)]
        col = [set() for _ in range(m)]
        square = [set() for _ in range(m)]

        for i in range(m):
            for j in range(m):
                if board[i][j] == ".":
                    continue

                sq_ind = (i // 3) * 3 + (j //3)
                val = board[i][j]
                if val in row[i] or val in col[j] or val in square[sq_ind]:
                    return False

                row[i].add(val)
                col[j].add(val)
                square[sq_ind].add(val)

        return True