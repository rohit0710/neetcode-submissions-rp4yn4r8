class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        graph= defaultdict(set)
        DIR = [0,1,0,-1,1,0,-1,0]
        largest_numbers = deque()
        m,n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                for k in range(0,8, 2):
                    nr,nc = i + DIR[k], j +DIR[k+1]
                    if not 0 <= nr <m or not 0 <= nc < n or matrix[i][j] >= matrix[nr][nc]:
                        continue
                    
                    graph[(i,j)].add((nr,nc))
                if len(graph[(i,j)]) == 0:
                    largest_numbers.append((i,j))
        
        level = 0
        while largest_numbers:
            level += 1
            for _ in range(len(largest_numbers)):
                i,j = largest_numbers.popleft()
                for k in range(0, 8, 2):
                    nr, nc = i + DIR[k], j + DIR[k + 1]
                    if not 0 <= nr < m or not 0 <= nc < n or matrix[i][j] <= matrix[nr][nc]:
                        continue
                    graph[(nr,nc)].remove((i,j))
                    if len(graph[(nr, nc)]) == 0:
                        largest_numbers.append((nr, nc))
        
        return level