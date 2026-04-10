class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])
        
        def dfs(i,j):
            if not 0<=i<m or not 0<=j<n or board[i][j]!= 'O':
                return 
            board[i][j] = 'S'
            dfs(i+1,j)
            dfs(i, j+1)
            dfs(i, j-1)
            dfs(i-1, j)
        
        for row in range(m):
            if board[row][0] == 'O':
                dfs(row, 0)
            if board[row][n-1] == 'O':
                dfs(row, n-1)

        for col in range(n):
            if board[0][col] == 'O':
                dfs(0, col)
            if board[m-1][col] == 'O':
                dfs(m-1, col)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'S':
                    board[i][j] = 'O'