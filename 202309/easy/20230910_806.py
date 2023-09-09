## https://leetcode.com/problems/number-of-lines-to-write-string/

class Solution(object):
    def numberOfLines(self, widths, s):
        """
        :type widths: List[int]
        :type s: str
        :rtype: List[int]
        """
        r, cnt = 1, 0
        for s_ in s :
            n = widths[ord(s_)-97]
            if cnt + n <= 100 : cnt += n
            else :
                r += 1
                cnt = n
        return [r, cnt]