## https://leetcode.com/problems/find-the-difference/

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        for l in t :
            if l in s :
                s = s.replace(l, '', 1)
            else : return l
        
        return s