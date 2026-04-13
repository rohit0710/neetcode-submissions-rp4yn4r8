class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        que = deque()
        m,n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    que.append((i,j,0))
        dir = [(1,0), (-1,0), (0, 1), (0, -1)]
        
        while que:
            for _ in range(len(que)):
                i,j,t = que.popleft()

                for d in dir:
                    r,c = i + d[0], j + d[1]

                    if 0 <= r < m and 0 <= c < n and grid[r][c] > t + 1:
                        grid[r][c] = t + 1
                        que.append((r,c, t+1))


