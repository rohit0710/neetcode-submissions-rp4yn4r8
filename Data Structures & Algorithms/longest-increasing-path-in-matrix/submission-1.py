class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dir = [(1,0), (-1, 0), (0, 1), (0, -1)]
        graph = defaultdict(set)
        que = deque()
        m,n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                for d in dir:
                    r,c = i + d[0], j + d[1]
                    if not 0 <= r < m or not 0 <= c < n or matrix[r][c] >= matrix[i][j]:
                        continue
                    graph[(i,j)].add((r,c))
                if not graph[(i,j)]:
                    que.append((i,j))
        
        res = 0

        while que:
            res += 1
            for _ in range(len(que)):
                i,j = que.popleft()
                for d in dir:
                    r,c = i + d[0], j + d[1]
                    if not 0 <= r < m or not 0 <= c < n or matrix[r][c] <= matrix[i][j]:
                        continue
                    graph[(r,c)].remove((i,j))
                    if not graph[(r,c)]:
                        que.append((r,c))

        return res
                