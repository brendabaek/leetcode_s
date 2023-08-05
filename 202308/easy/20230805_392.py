## https://leetcode.com/problems/is-subsequence/

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        for l in s :
            if l not in t : return False
            t = t[t.index(l)+1:]
        return True