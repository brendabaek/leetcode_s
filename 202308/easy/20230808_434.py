## https://leetcode.com/problems/number-of-segments-in-a-string/

class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 : return 0
        ans = []

        while s != "" :
            s = s.strip(" ")
            if len(s) == 0 : break

            if " " in s :
                idx = s.index(" ")
                ans.append(s[:idx])
                s = s[idx+1:]
            else :
                ans.append(s)
                break
                
        return len(ans)