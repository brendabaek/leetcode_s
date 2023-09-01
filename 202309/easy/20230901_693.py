## https://leetcode.com/problems/binary-number-with-alternating-bits/

class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n = bin(n)[2:]
        for i in range(1, len(n)) :
            if n[i-1] == n[i] : return False
        return True