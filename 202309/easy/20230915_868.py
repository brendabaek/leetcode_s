## https://leetcode.com/problems/binary-gap/

class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        bin_n = bin(n)[2:]
        ln = len(bin_n)
        for i in range(ln) :
            if bin_n[i] == "1" :
                try :
                    left, right = right, i
                    ans = max(right-left, ans)
                except : right, ans = i, 0
        return ans