#P1- Rotate Array
class Solution(object):
    def rotate(self, nums, k):
        l, r = 0, len(nums) - 1
        def rev(nums, l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l + 1, r - 1
        
        k = k % len(nums)
        rev(nums, 0, len(nums) - 1)
        rev(nums, 0, k - 1)
        rev(nums, k, len(nums) - 1)

# Test case 1:
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
solution = Solution()
solution.rotate(nums, k)
print(nums)  # Output: [5, 6, 7, 1, 2, 3, 4]

#P2- BEST-TIME-TO-BUY-AND-SELL-STOCK
class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        
        min_price = prices[0]
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)
        
        return max_profit

# Test case:
prices = [7, 1, 5, 3, 6, 4]
solution = Solution()
print(solution.maxProfit(prices))
