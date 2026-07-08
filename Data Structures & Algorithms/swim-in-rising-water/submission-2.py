class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap = []
        heapq.heappush(heap, ( grid[0][0], 0, 0))
        m, n = len(grid), len(grid[0])
        dir = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        visited = [[False] * n for _ in range(m)]
        visited[0][0] = True
        while heap:
            time, i, j = heapq.heappop(heap)

            if i == m - 1 and j == n - 1:
                return time
            
            for d in dir:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < m and 0 <= nj < n and not visited[ni][nj]:
                    heapq.heappush(heap, (max(time, grid[ni][nj]), ni, nj))
                    visited[ni][nj] = True
        return -1