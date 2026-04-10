class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cur_sum = 0
        res = 0
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1
        for num in nums:
            cur_sum += num
            diff = cur_sum - k

            res += prefix_sum[diff]
            prefix_sum[cur_sum] += 1
        return res