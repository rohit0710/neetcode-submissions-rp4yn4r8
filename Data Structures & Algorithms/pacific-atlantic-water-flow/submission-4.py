class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        m,n = len(grid), len(grid[0])

        pcorner, acorner = deque(), deque()
        
        for i in range(m):
            pcorner.append((i, 0))
            acorner.append((i, n-1))


        for j in range(n):
            pcorner.append((0, j))
            acorner.append((m-1, j))
        dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        def dfs(que):
            visited = [[False] * n for _ in range(m)]
            res = set()

            while que:
                i, j = que.popleft()

                res.add((i, j))
                visited[i][j] = True
                for d in dir:
                    ni, nj = i + d[0], j + d[1]
                    if 0 <= ni < m and 0 <= nj < n and not visited[ni][nj] and grid[ni][nj] >= grid[i][j]:
                        que.append((ni, nj))
            
            return res
        
        pacific = dfs(pcorner)
        atlantic = dfs(acorner)

        return list(pacific & atlantic)
