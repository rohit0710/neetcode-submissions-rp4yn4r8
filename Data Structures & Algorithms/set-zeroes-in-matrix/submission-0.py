class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        is_first_col_zero = False
        for i in range(m):
            if matrix[i][0] == 0:
                is_first_col_zero = True
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1,m):
            for j in range(1, n):
                matrix[i][j] = 0 if matrix[i][0] == 0 or matrix[0][j] == 0 else matrix[i][j]

        
        if matrix[0][0] == 0:
            for j in range(n):
                matrix[0][j] = 0
        
        if is_first_col_zero:
            for i in range(m):
                matrix[i][0] = 0

