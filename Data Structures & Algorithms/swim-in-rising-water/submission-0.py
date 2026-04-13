class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        dir = [(1,0), (-1, 0), (0, 1), (0, -1)]

        heap = [(grid[0][0], 0, 0)]
        res = 0
        m,n = len(grid), len(grid[0])
        visited = set()

        while heap:
            level, i, j = heapq.heappop(heap)

            res = max(res, level)
            if i == m-1 and j == n-1:
                return res

            for d in dir:
                r,c = i + d[0], j + d[1]

                if not 0 <= r < m or not 0 <= c < n or (r,c) in visited:
                    continue

                visited.add((r,c))
                heapq.heappush(heap, (grid[r][c], r, c))

        return res                

