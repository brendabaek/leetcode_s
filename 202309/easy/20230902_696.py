## https://leetcode.com/problems/count-binary-substrings/

class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans, m = 0, 1
        for i in range(1, len(s)) :
            if s[i-1] == s[i] : m += 1
            else :
                for j in range(min(m, len(s)-i)) :
                    if s[i+j] != s[i-j-1] : ans += 1
                    else : break
                m = 1
        return ans

        