class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        neg= float("-inf")
        hold, reset, sold = neg, 0, neg

        for p in prices:
            temp = sold
            sold = hold + p
            hold = max(hold, reset - p)
            reset = max(reset, temp)
        
        return max(sold, reset)