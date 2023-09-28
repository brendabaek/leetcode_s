## https://leetcode.com/problems/remove-outermost-parentheses/

class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stt, cnt, ans = 0, 0, ''
        for i in range(len(s)) :
            if s[i] == "(" : cnt += 1
            else : cnt -= 1
            if cnt == 0 :
                ans += s[stt+1:i]
                stt = i+1
        return ans