#P1- Minimum Number of Arrows to Burst Balloons
class Solution(object):
    def findMinArrowShots(self, points):
        if not points:
            return 0
        
        points.sort(key=lambda x: x[1])
        arrows = 1
        curr_arrow = points[0][1]
        
        for point in points:
            if point[0] > curr_arrow:
                arrows += 1
                curr_arrow = point[1]
        
        return arrows

#P2- Min Stack
class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if self.stack:
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]
        return None

    def getMin(self):
        if self.min_stack:
            return self.min_stack[-1]
        return None
