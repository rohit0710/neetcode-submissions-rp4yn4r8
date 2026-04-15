class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        grid = [[0 for _ in  range(len(text2)+1)] for _ in range(len(text1)+1)]
        m, n = len(text1), len(text2)
        for i in range(1,m+1):
            for j in range(1, n+ 1):
                if text1[i-1] == text2[j-1]:
                    grid[i][j] = 1 + grid[i-1][j-1]
                else:
                    grid[i][j] = max(grid[i-1][j], grid[i][j-1])
        
        return grid[-1][-1]