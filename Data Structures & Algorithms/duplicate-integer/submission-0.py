class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq_map = set()
        for i in nums:
            if i in freq_map:
                return True
            else:
                freq_map.add(i)
        
        return False