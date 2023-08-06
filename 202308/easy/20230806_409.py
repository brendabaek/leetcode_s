## https://leetcode.com/problems/longest-palindrome/

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = 0
        ans = 0
        while cnt < len(s)-1:
            l = s[cnt]
            if l in s[cnt+1:] :
                ans += 2
                s = s.replace(l, '', 2)
            else : cnt += 1

        if len(s) > 0 : return ans+1
        else : return ans
