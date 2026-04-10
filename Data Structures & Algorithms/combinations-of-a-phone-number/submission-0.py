class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        charmap = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []
        def helper(word, digits):
            if not digits:
                res.append(word)
                return
            for ch in charmap[digits[0]]:
                helper(word + ch, digits[1:])

        helper("", digits)
        return res

