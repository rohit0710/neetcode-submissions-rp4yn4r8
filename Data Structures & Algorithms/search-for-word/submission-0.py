class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n = len(board), len(board[0])
        def backtrack(word, i, j):
            if len(word) == 0:
                return True

            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[0]:
                return False


            temp = board[i][j]
            board[i][j] = "."
            ans = backtrack(word[1:], i - 1, j ) or backtrack( word[1:], i + 1, j ) or backtrack( word[1:], i, j-1 ) or backtrack( word[1:], i, j + 1 )
            board[i][j] = temp

            return ans

        for i in range(m):
            for j in range(n):
                if backtrack( word, i, j):
                    return True
        return False