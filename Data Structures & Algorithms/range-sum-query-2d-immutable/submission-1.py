class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.maxtrix = matrix
        self.m, self.n = len(matrix), len(matrix[0])
        self.precompute_mat = [[0 for _ in range(self.n + 1)] for _ in range(self.m+1)]

        for i in range(self.m):
            prefix = 0
            for j in range(self.n):
                prefix += matrix[i][j]
                above = self.precompute_mat[i][j+1]
                self.precompute_mat[i+1][j+1] = prefix + above
        print(self.precompute_mat)
    
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        bottomRight = self.precompute_mat[row2+1][col2+1]   
        above = self.precompute_mat[row1][col2+1]
        left = self.precompute_mat[row2+1][col1]
        topLeft = self.precompute_mat[row1][col1]

        return bottomRight - above - left + topLeft

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)