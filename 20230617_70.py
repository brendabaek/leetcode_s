## https://leetcode.com/problems/climbing-stairs/

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 : return 1

        ans = 1

        for i in range(1, (n//2)+1) :
            ln = n - i
            cnt = 1
            dist = 1

            for j in range(ln, ln-i, -1) :
                cnt *= j
                cnt /= dist
                dist += 1
            
            ans += cnt
        
        return ans