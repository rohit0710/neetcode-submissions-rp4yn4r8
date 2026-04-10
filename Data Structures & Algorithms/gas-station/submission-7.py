class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        pos = 0
        capacity = 0
        for i in range(len(gas)):
            capacity += gas[i] - cost[i]
            if capacity < 0 :
                capacity = 0
                pos = i + 1
        return pos