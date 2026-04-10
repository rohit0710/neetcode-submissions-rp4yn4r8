class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que = deque()
        res = []

        for i in range(k):
            while que and nums[que[-1]] <= nums[i]:
                que.pop()
            que.append(i)
        res.append(nums[que[0]])

        for i in range(k, len(nums)):
            if i >= que[0] + k:
                que.popleft()

            while que and nums[que[-1]] <= nums[i]:
                que.pop()
            que.append(i)

            res.append(nums[que[0]])

        return res