## https://leetcode.com/problems/word-pattern/

class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """

        if pattern == None or s == None : return False

        dics = {}
        words = s.split(' ')

        if len(pattern) != len(words) : return False
        ln = len(pattern)
        for i in range(ln):
            p = pattern[i]
            word = words[i]
            if p not in dics :
                if word not in dics.values() :
                    dics[p] = word
                else : return False
            else :
                if dics[p] != word : return False
        
        return True