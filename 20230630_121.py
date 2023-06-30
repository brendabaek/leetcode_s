## https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ln = len(prices)
        if ln <= 1 : return 0
        
        stt_idx = 0
        end_idx = ln-1

        for i in range(ln-1) :
            if prices[i] > prices[i+1] : continue
            else :
                stt_idx = i
                break

        for i in range(ln-1, 0, -1) :
            if prices[i] < prices[i-1] : continue
            else :
                end_idx = i+1
                break
        
        new_prices = prices[stt_idx:end_idx]
        return self.find_range(new_prices)



    def find_range(self, prices, ans=0) :
        ln = len(prices)

        for i in range(ln) :
            if i == ln-1 : return ans
            elif prices[i] > prices[i+1] : continue
            else :                
                new_price = prices[i:]
                pf = max(new_price) - new_price[0]
                if ans < pf : ans = pf
                if new_price[0] == min(new_price) : return ans

        return ans