## https://leetcode.com/problems/arranging-coins/

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        num, ans = 1, 1
        while num <= n :
            num += ans
            ans += 1
        if num - 1 == n : return ans-1
        else : return ans-2


class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 1
        while n - ans >= 0 :
            n -= ans
            ans += 1            
        return ans-1