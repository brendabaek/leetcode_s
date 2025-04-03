## https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/

class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        s = list(s)
        for word in words :
            try :
                if word[0] == s[0] : s.pop(0)
                else : return False
            except : return False
        return s == []