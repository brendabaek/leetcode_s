## https://leetcode.com/problems/sqrtx/

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x == 0 : return 0
        sqr = (len(str(x))-1) // 2
        ans = 0

        while sqr >= 0 :
            for i in range(9, 0, -1) :
                root = ans + (i * (10 ** sqr))
                if x < (root * root) : continue
                else :
                    ans = root
                    break
            sqr -= 1

        return ans