class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minv, maxv = min(nums), max(nums)
        freq = [0] * (maxv - minv  + 1)

        for num in nums:
            freq[num-minv] += 1

        for i in range(len(freq)-1, -1, -1):
            if freq[i] != 0:
                k -= freq[i]
                if k <= 0:
                    return minv+i

        return minv