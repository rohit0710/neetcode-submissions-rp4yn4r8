class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        que = deque()
        m, n = len(grid), len(grid[0])
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    que.append((i,j))
        if fresh == 0:
            return 0
        
        dir = [(1,0), (0, 1), (-1 ,0), (0, -1)]
        time = -1
        while que:
            time += 1
            print(que)
            for _ in range(len(que)):
                i, j = que.popleft()
                for d in dir:
                    ni, nj = i + d[0], j + d[1]
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                        fresh -= 1
                        que.append((ni, nj))
                        grid[ni][nj] = 2
                        print("Coming inside", ni, nj)

        
        print(time, fresh)
        return time if fresh == 0 else -1