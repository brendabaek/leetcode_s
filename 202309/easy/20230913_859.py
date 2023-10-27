## https://leetcode.com/problems/buddy-strings/

class Solution(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """

        if len(s) != len(goal) : return False
        if s == goal :
            dics = {}
            for s_ in s :
                try :
                    dics[s_] += 1
                    return True
                except : dics[s_] = 1

        ln, l1, l2 = len(s), '', ''
        for i in range(ln) :
            if s[i] != goal[i] :
                l1 += s[i]
                l2 += goal[i]
            if len(l1) > 2 : return False
            
        if l1 == '' : return False
        elif l1 == l2[::-1] : return True
        else : return False