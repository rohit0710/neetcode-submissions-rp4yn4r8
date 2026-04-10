class Solution:
    def isValid(self, s: str) -> bool:
        map_ = {"}": "{", "]": "[", ")":"("}
        stack = []
        for i in s:
            if i not in map_.keys():
                stack.append(i)
            else:
                if stack and map_[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False