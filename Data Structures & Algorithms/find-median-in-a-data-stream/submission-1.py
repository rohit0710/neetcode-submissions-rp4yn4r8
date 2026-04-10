class MedianFinder:

    def __init__(self):
        self.low = []
        self.high =[]
        heapq.heapify(self.low)
        heapq.heapify(self.high)
        
    def addNum(self, num: int) -> None:
        if len(self.low) == len(self.high):
            heapq.heappush(self.low, -heapq.heappushpop(self.high, num))
        else:
            heapq.heappush(self.high, -heapq.heappushpop(self.low, -num))
        
    def findMedian(self) -> float:
        if len(self.low) == len(self.high):
            return (self.high[0] - self.low[0]) / 2
        else:
            return -self.low[0]