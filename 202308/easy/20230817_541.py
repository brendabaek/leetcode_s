## https://leetcode.com/problems/reverse-string-ii/description/

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        ans, cnt = '', 0
        while k * cnt <= len(s) :
            if cnt == 0 : ans += s[(k*(cnt+1))-1::-1] + s[k*(cnt+1):k*(cnt+2)]
            else : ans += s[(k*(cnt+1))-1:(k*cnt)-1:-1] + s[k*(cnt+1):k*(cnt+2)]
            cnt += 2
        return ans