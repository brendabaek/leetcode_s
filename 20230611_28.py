## https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        ln_n = len(needle)
        ln_h = len(haystack)

        if ln_h == 0 and ln_n == 0 : return 0
        elif ln_n == 0 or ln_h == 0 : return -1
        elif ln_h < ln_n : return -1
        else :
            for i in range(ln_h-ln_n+1) :
                if haystack[i:i+ln_n] == needle :
                    return i
            return -1