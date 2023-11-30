## https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ln, ans = len(prices), []
        for i in range(ln) :
            check = False
            p = prices[i]
            for j in range(i+1, ln) :
                if p > prices[j] :
                    ans.append(p-prices[j])
                    check = True
                    break
                elif p == prices[j] :
                    ans.append(0)
                    check = True
                    break
            if check == False : ans.append(p)
        return ans           