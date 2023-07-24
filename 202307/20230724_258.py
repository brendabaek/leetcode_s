## https://leetcode.com/problems/add-digits/description/

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        if num == None : return

        while True :
            ans = 0
            while num // 10 != 0 :
                ans += num % 10
                num = num // 10
            ans += num
            if ans < 10 : return ans
            else : num = ans