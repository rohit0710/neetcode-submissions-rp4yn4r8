class Solution:
    def spiralOrder(self, grid ) -> List[int]:
        m,n = len(grid), len(grid[0])
        dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cur_dir, change_dir = 0, 0
        res = [grid[0][0]]
        vis = "visited"
        grid[0][0] = vis
        i,j = 0, 0
        while change_dir < 2:
            while True:
                ni = i + dir[cur_dir][0]
                nj = j + dir[cur_dir][1]

                if not 0 <= ni < m or not 0 <= nj < n or grid[ni][nj] == vis:
                    break
                
                change_dir = 0
                res.append(grid[ni][nj])
                grid[ni][nj] = vis

                i = ni
                j = nj
            
            cur_dir = (cur_dir + 1) % 4
            change_dir += 1
        print(grid)
        return res
