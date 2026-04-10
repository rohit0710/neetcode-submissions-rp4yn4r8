class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        curr= 0
        res = 0

        for i, v in enumerate(gas):
            res += gas[i] - cost[i]
            if res < 0:
                curr = i + 1
                res = 0

        return curr
