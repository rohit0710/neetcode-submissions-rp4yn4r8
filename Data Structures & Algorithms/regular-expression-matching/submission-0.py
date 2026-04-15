class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def match(pattern, text):
            if not pattern:
                return not text

            first = bool(text) and pattern[0] in {text[0], "."}

            if len(pattern) > 1 and pattern[1] == "*":
                return match(pattern[2:], text) or (first and match(pattern, text[1:]))
            return first and match(pattern[1:], text[1: ])
        return match(p, s)