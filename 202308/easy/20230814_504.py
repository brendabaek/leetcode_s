## https://leetcode.com/problems/base-7/description/

class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num > 0 : ans = ''
        elif num < 0 : ans = '-'
        else : return "0"
        num = abs(num)

        cnt = 0
        while (7 ** cnt) <= num : cnt += 1
        while cnt > 0 :
            cnt -= 1
            ans += str(num // (7 ** cnt))
            num = num % (7 ** cnt)
            
        return ans