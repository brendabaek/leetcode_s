## https://leetcode.com/problems/multiply-strings/

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0" : return "0"
        elif num1 == "1" : return num2
        elif num2 == "1" : return num1
        
        n1, n2 = 0, 0
        for n in num1 : n1 = (n1 * 10) + int(n)
        for n in num2 : n2 = (n2 * 10) + int(n)
        a, ans = n1 * n2, ''
        while a > 0 :
            ans = str(a % 10) + ans
            a = a // 10
        return ans
        
