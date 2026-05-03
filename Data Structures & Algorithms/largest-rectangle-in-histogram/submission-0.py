class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        area = 0

        for i,v in enumerate(heights):
            while stack[-1] != -1 and heights[stack[-1]] >= v:
                area = max(area, heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i)
        
        while stack[-1] != -1:
            area = max(area, heights[stack.pop()] * (len(heights) - stack[-1] - 1))
        
        return area