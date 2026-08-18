class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        heap = []
        dir = [(1, 0), (0, 1), (0, -1), (-1, 0)]

        heapq.heappush(heap, (grid[0][0], 0, 0))
        visited = [[False]*n for _ in range(m)]
        visited[0][0] = True
        while heap:
            height, i, j = heapq.heappop(heap)

            if i == m -1 and j == n-1:
                return height
            
            for d in dir:
                ni, nj = i + d[0], j + d[1]

                if 0 <= ni < m and 0 <= nj < n and not visited[ni][nj]:
                    visited[ni][nj] = True
                    heapq.heappush(heap, (max(height, grid[ni][nj]), ni, nj))
        
        return 0