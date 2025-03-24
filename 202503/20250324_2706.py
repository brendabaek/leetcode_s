## https://leetcode.com/problems/buy-two-chocolates/

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        price = min(prices)
        prices.remove(price)
        price += min(prices)
        return money - price if money - price >= 0 else money