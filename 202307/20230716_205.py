## https://leetcode.com/problems/isomorphic-strings/

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if s == None or t == None or (len(s) != len(t)) : return False

        dics1 = {}
        dics2 = {}
        ln = len(s)
        ans1 = True
        ans2 = True

        for i in range(ln) :
            s_ = s[i]
            t_ = t[i]

            if s_ in dics1 : ans1 = (dics1[s_] == t_)
            else : dics1[s_] = t_
            if t_ in dics2 : ans2 = (dics2[t_] == s_)
            else : dics2[t_] = s_
            if ans1 == False or ans2 == False : return False
        return True