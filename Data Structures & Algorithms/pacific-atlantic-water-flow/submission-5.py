class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        m,n = len(grid), len(grid[0])
        
        def dfs(que):
            res = set()
            visited = [[False] * n for _ in range(m)]
            while que:
                i, j = que.popleft()
                res.add((i, j))
                visited[i][j] = True
                for d in dir:
                    ni, nj = i + d[0], j + d[1]
                    if 0 <= ni < m and 0 <= nj <n and not visited[ni][nj] and grid[ni][nj] >= grid[i][j]:
                        que.append((ni,nj))
                        visited[ni][nj]
            
            return res

        p_que, a_que = deque(), deque()
        for i in range(m):
            p_que.append((i, 0))
            a_que.append((i, n-1))
        
        for j in range(n):
            p_que.append((0, j))
            a_que.append((m-1, j))

        pacific = dfs(p_que)
        atlantic = dfs(a_que)

        return list(pacific & atlantic)