## https://leetcode.com/problems/license-key-formatting/

class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = s.upper().replace('-', '')
        stt = len(s) % k
        spl = len(s) / k
        ans, s = s[:stt], s[stt:]
        while len(s) > 0 :
            if ans == '' : ans = s[:k]
            else : ans = ans + '-' + s[:k]
            s = s[k:]
        return ans