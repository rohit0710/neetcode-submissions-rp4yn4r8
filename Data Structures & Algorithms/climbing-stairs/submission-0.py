class Solution:
    def climbStairs(self, n: int) -> int:
        res = [1, 2]
        if n == 1:
            return res[0]
        if n == 2:
            return res[1]
        for i in range(2, n):
            res.append(res[-1]+ res[-2])
        
        return res[-1]