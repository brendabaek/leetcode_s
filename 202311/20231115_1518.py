## https://leetcode.com/problems/water-bottles/

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        b, e = numBottles, 0
        while b >= numExchange :
            e = b % numExchange
            b = b // numExchange
            ans += b
            b, e = b+e, 0
        return ans