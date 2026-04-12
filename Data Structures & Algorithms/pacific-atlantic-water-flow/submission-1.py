class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:
        def bfs(que):
            res = set()
            visited = set()
            while que:
                i, j = que.popleft()
                visited.add((i,j))
                res.add((i,j))
                for d in dir:
                    r, c = i + d[0], j + d[1]

                    if 0 <= r < m and 0 <= c < n and (r,c) not in visited and grid[r][c] >= grid[i][j]:
                        que.append((r,c))
            return res

        dir = [(0, 1), (0,-1), (1,0), (-1, 0)]
        m,n = len(grid), len(grid[0])
        p_que= deque()
        a_que= deque()
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    p_que.append((i,j))
                if i == m-1 or j == n-1:
                    a_que.append((i,j))
        
        pacific = bfs(p_que)
        atlantic = bfs(a_que)
        print(pacific & atlantic)
        return list( pacific & atlantic)



        