import heapq  # by default min heap


class MedianFinder:

    def __init__(self):
        # max_heap (negate values to work with library) # fill this up first, so might only be bigger by 1 at most
        self.small_heap = []
        self.large_heap = []  # min_heap
        self.total_elems = 0
        return

    def addNum(self, num: int) -> None:
        self.total_elems += 1

        if len(self.small_heap) == 0:  # large_heap also 0
            heapq.heappush(self.small_heap, -num)
        elif len(self.small_heap) - len(self.large_heap) >= 1:  # diff = 0
            # just add to small_heap (with adjustments)

            # this value should still be smaller than smallest value in large_heap min_heap
            max_overflow_small_heap = -heapq.heappushpop(self.small_heap, -num)
            heapq.heappush(self.large_heap, max_overflow_small_heap)
        elif len(self.small_heap) == len(self.large_heap):
            min_overflow_large_heap = heapq.heappushpop(self.large_heap, num)
            heapq.heappush(self.small_heap, -min_overflow_large_heap)

        # print(self.small_heap, self.large_heap)

        return

    def findMedian(self) -> float:
        if self.total_elems % 2:
            # true --> 1 --> odd
            return -self.small_heap[0]
        else:
            return (-self.small_heap[0] + self.large_heap[0])/2


# Your MedianFinder object will be instantiated and called as such:
medianFinder = MedianFinder()
medianFinder.addNum(1)
medianFinder.addNum(2)
print(medianFinder.findMedian())
medianFinder.addNum(3)
print(medianFinder.findMedian())
