class Solution:
    def trap(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        lmax, rmax = 0,0
        ans = 0
        while l < r:
            if heights[l] < heights[r]:
                if heights[l] <= lmax:
                    ans += lmax - heights[l]
                else:
                    lmax = heights[l]
                l += 1
            else:
                if heights[r] <= rmax:
                    ans += rmax - heights[r]
                else:
                    rmax = heights[r]
                r -= 1
        return ans