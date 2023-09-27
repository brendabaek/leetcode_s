## https://leetcode.com/problems/complement-of-base-10-integer/

class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 : return 1
        else : cnt = 1
        while cnt <= n : cnt *= 2
        return cnt-1-n
