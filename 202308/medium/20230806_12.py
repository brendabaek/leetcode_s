## https://leetcode.com/problems/integer-to-roman/

dics = {0:"", 1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ans = ''
        cnt = 1

        for i in range(len(str(num))):
            n = num % 10
            if n < 4 :
                ans = (dics[cnt] * n) + ans
            elif n == 4 :
                ans = dics[cnt] + dics[5*cnt] + ans
            elif n < 9 :
                ans = dics[5*cnt] + (dics[cnt] * (n-5)) + ans
            elif n == 9 :
                ans = dics[cnt] + dics[10*cnt] + ans            
            cnt *= 10
            num = num // 10
        return ans