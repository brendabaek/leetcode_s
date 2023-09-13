## https://leetcode.com/problems/backspace-string-compare/

class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        new_s, new_t = '', ''
        for s_ in s :
            if s_ == '#' : new_s = new_s[:-1]
            else : new_s += s_
        for t_ in t :
            if t_ == '#' : new_t = new_t[:-1]
            else : new_t += t_
        return new_s == new_t