## https://leetcode.com/problems/reverse-integer/

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x == 0 or x == None : return 0
        elif x > 0 :
            ans = x % 10
            while x // 10 > 0 :
                x = x // 10
                ans = (ans * 10) + (x % 10)
            if ans > ((2**31)-1) : return 0
            else : return ans

        elif x < 0 :
            x = x * (-1)
            ans = x % 10
            while x // 10 > 0 :
                x = x // 10
                ans = (ans * 10) + (x % 10)        
            if ans > (2**31) : return 0
            else : return -ans