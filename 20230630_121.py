## https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution(object):
    
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1 : return 0
        
        buy = 0
        sell = 1
        ans = 0

        while sell < len(prices) :
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                ans = max(ans, profit)
            else :
                buy = sell
            sell += 1
        
        return ans