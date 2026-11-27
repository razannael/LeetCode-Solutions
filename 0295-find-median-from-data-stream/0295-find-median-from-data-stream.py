import bisect
class MedianFinder:

    def __init__(self):
        self.l = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.l, num)
        

    def findMedian(self) -> float:
        le = len(self.l)
        if le%2 == 0:
            le //= 2
            return (self.l[le-1] + self.l[le])/2
        else:
            le //= 2
            return self.l[le]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()