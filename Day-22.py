#P1- Factorial Trailing Zeroes
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        i = 5
        while n // i >= 1:
            count += n // i
            i *= 5
        return count
#P2- Find Median from Data Stream
import heapq

class MedianFinder(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # max heap to store the smaller half of the numbers
        self.max_heap = []
        # min heap to store the larger half of the numbers
        self.min_heap = []

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: None
        """
        # Add the number to the correct heap
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        
        # Balance the two heaps
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        # If the total number of elements is odd, the median is the top of the max heap
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        # If the total number of elements is even, the median is the average of the top of the max heap and the top of the min heap
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
