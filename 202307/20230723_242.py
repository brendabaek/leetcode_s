## https://leetcode.com/problems/valid-anagram/

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == t : return True
        if len(s) != len(t) : return False
        dics = {}
        for l in s :
            if l in dics : dics[l] += 1
            else : dics[l] = 1
        for l in t :
            if l in dics : dics[l] -= 1
            else : return False
        for cnt in dics.values() :
            if cnt != 0 : return False
        return True