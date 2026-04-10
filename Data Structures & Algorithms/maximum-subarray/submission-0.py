class Solution:
    def maxSubArray(self, arr: List[int]) -> int:
        if not arr:
            return 0
        res = arr[0]
        maxv = arr[0]
        temp = 0
        for n in arr[1:]:
            maxv = max(n, n+maxv)
            res = max(maxv, res)

        return res