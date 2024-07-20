#P1- MAXIMUM SUM CIRCULAR SUBARRAY
class Solution(object):
    def maxSubarraySumCircular(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        max_sum = float('-inf')
        min_sum = float('inf')
        total_sum = 0
        curr_max_sum = 0
        curr_min_sum = 0

        for num in nums:
            total_sum += num
            curr_max_sum = max(num, curr_max_sum + num)
            max_sum = max(max_sum, curr_max_sum)
            curr_min_sum = min(num, curr_min_sum + num)
            min_sum = min(min_sum, curr_min_sum)

        if max_sum > 0:
            return max(max_sum, total_sum - min_sum)
        else:
            return max_sum
          
#-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X-X

#P2-KOKO EATING BANANAS

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        def canEatAllBananas(speed):
            return sum((pile - 1) // speed + 1 for pile in piles) <= h

        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2
            if canEatAllBananas(mid):
                right = mid
            else:
                left = mid + 1

        return left
