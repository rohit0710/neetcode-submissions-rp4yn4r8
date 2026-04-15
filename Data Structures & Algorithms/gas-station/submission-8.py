class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum (cost):
            return -1
        cap = 0
        pos = 0
        for i in range(len(gas)):
            cap += gas[i] - cost[i]

            if cap < 0:
                pos = i+1
                cap = 0
        
        return pos