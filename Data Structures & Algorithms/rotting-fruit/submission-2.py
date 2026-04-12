class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        que = deque()
        fresh = 0
        m,n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    que.append((i,j,0))
                elif grid[i][j] == 1:
                    fresh += 1
        
        time = 0
        if fresh == 0:
            return 0 
        dir = [(0,1), (0,-1), (1,0), (-1,0)]
        while que:
            print(que)
            time += 1
            for _ in range(len(que)):
                i,j,t = que.popleft()
                for d in dir:
                    r,c = i + d[0], j + d[1]
                    if not 0 <= r < m or not 0<= c < n:
                        continue
                    
                    if grid[r][c] == 1:
                        grid[r][c] = 2
                        fresh -= 1
                        que.append((r,c, t + 1))
        
        return time-1 if fresh <= 0 else -1
