## https://leetcode.com/problems/number-complement/

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        cnt = 0
        while 2 ** cnt <= num : cnt += 1
        return (2 ** cnt) - 1 - num