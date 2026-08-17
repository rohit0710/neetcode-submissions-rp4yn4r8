class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        que = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    que.append((i, j, 0))
        
        dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while que:
            i, j, dist = que.popleft()
            for d in dir:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < m and 0 <= nj< n and grid[ni][nj] > dist + 1:
                    grid[ni][nj] = dist + 1
                    que.append((ni, nj, dist + 1))
        
