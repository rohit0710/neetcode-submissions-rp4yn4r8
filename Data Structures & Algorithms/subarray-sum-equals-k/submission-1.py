class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = defaultdict(int)
        cur_sum = 0
        res = 0
        prefix_sum[0] = 1
        for n in nums:
            cur_sum += n
            diff = cur_sum - k

            res += prefix_sum[diff]
            prefix_sum[cur_sum] += 1
        return res