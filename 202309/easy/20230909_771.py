## https://leetcode.com/problems/jewels-and-stones/

class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        ans = 0
        for i in jewels :
            try : ans += stones.count(i)
            except : pass
        return ans