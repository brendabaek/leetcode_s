## https://leetcode.com/problems/add-strings/

disc = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ans1, ans2 = 0, 0
        cnt = 0
        for l in num1 :
            ans1 = (ans1 * 10) + disc[l]
            cnt += 1
        
        cnt = 0
        for l in num2 :
            ans2 = (ans2 * 10) + disc[l]
            cnt += 1

        return str(ans1+ans2)