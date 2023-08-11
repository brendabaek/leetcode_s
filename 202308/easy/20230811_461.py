## https://leetcode.com/problems/hamming-distance/


class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x = bin(x)[2:]
        y = bin(y)[2:]
        ln = min(len(x), len(y))
        if len(x) == len(y) : ans = 0
        elif len(x) < len(y) : ans = y[:abs(len(x) - len(y))].count('1')
        else : ans = x[:abs(len(x) - len(y))].count('1')
        for i in range(1, ln+1) :
            if x[-i] == y[-i] : continue
            else : ans += 1
        return ans