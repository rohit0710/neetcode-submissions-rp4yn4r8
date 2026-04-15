class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        minv = min(hand)
        maxv = max(hand)
        freq= [0 for _ in range(maxv - minv + 1)]

        for n in hand:
            freq[n - minv] += 1
        
        res = []
        pos = 0
        while pos < len(freq):
            while pos < len(freq) and freq[pos] == 0:
                pos += 1
            if pos == len(freq):
                break
            for i in range(pos, pos+groupSize):
                if i >= len(freq) or freq[i] == 0:
                    return False
                freq[i] -= 1
        return True
                     
