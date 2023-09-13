## https://leetcode.com/problems/decode-ways/

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0] == "0" : return 0
        tmp1, tmp2, ans = 1, 1, 1

        for i in range(len(s)-1) :
            num = int(s[i:i+2])
            if num == 0 or (num > 26 and num % 10 == 0): return 0
            elif num == 10 or num == 20 :
                ans = ans * tmp1
                tmp1, tmp2 = 1, 1
            elif num < 10 or num > 26:
                ans = ans * tmp2
                tmp1, tmp2 = 1, 1
            else : tmp1, tmp2 = tmp2, tmp1+tmp2
        return ans * tmp2