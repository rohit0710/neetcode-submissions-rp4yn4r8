from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_map = defaultdict(list)
        for s in  strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord('a')] += 1
            word_map[tuple(count)].append(s)

        return list(word_map.values())
        