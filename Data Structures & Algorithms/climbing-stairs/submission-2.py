class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        h1, h0= 2, 1
        for i in range(2, n):
            temp = h1
            h1 = h1 + h0
            h0 = temp

        return h1