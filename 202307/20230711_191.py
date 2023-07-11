## https://leetcode.com/problems/number-of-1-bits/submissions/

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n == None : return
        ans = 0
        while n > 0 :
            if n % 2 == 1 :ans += 1
            n = n // 2
        return ans