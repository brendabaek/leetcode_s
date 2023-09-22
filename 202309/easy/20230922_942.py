## https://leetcode.com/problems/di-string-match/

class Solution(object):
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        down, up, ans = 0, len(s), []
        for s_ in s :
            if s_ == "I" :
                ans.append(down)
                down += 1
            else :
                ans.append(up)
                up -= 1
        ans.append(up)
        return ans