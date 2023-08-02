## https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ln = len(s)
        if ln < 2 : return ln
        a = ''
        ans = 1
        
        for i in range(ln) :
            if s[i] not in a :
                a += s[i]
            else :
                ans = max(ans, len(a))
                cnt = a.find(s[i])
                a = a[cnt+1:] + s[i]
        ans = max(ans, len(a))
        return ans