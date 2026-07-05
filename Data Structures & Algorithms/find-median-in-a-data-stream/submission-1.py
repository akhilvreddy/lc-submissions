import heapq

class MedianFinder:
    # max heap for lower half
    # min heap for greater half

    def __init__(self):
        self.lower = []
        self.greater = []
        
    def addNum(self, num: int) -> None:
        if self.greater and num < self.greater[0]:
            heapq.heappush(self.lower, -num)
        else:
            heapq.heappush(self.greater, num)

        if len(self.lower) > len(self.greater) + 1:
            heapq.heappush(self.greater, -heapq.heappop(self.lower))
        elif len(self.greater) > len(self.lower) + 1:
            heapq.heappush(self.lower, -heapq.heappop(self.greater))
        
        print(self.lower, self.greater)

        

    def findMedian(self) -> float:
        if len(self.lower) == len(self.greater):
            return (-self.lower[0] + self.greater[0]) / 2
        elif len(self.lower) > len(self.greater):
            return -self.lower[0]
        else:
            return self.greater[0]
        
        