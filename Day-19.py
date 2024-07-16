#P1- Best Time to Buy and Sell Stock III
class Solution:
    def maxProfit(self, prices):
        if not prices or len(prices) < 1:
            return 0
        buy1, sell1, buy2, sell2 = -prices[0], 0, -prices[0], 0
        for i in range(1, len(prices)):
            buy1 = max(buy1, -prices[i])
            sell1 = max(sell1, buy1 + prices[i])
            buy2 = max(buy2, sell1 - prices[i])
            sell2 = max(sell2, buy2 + prices[i])
        return sell2
#P2-Best Time to Buy and Sell Stock IV
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices or k == 0:
            return 0
        
        if k >= len(prices) // 2:
            return sum(max(0, b - a) for a, b in zip(prices, prices[1:]))
        
        dp = [[0] * len(prices) for _ in range(k + 1)]
        for i in range(1, k + 1):
            max_diff = -prices[0]
            for j in range(1, len(prices)):
                dp[i][j] = max(dp[i][j - 1], prices[j] + max_diff)
                max_diff = max(max_diff, dp[i - 1][j] - prices[j])
        
        return dp[k][-1]
