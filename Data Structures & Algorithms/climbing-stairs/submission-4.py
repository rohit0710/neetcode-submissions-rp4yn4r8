class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        h0, h1 = 0, 1

        for i in range(n):
            temp = h1 
            h1 = h1 + h0
            h0 = temp
        
        return h1