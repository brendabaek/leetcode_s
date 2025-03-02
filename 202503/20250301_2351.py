## https://leetcode.com/problems/first-letter-to-appear-twice/

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        lst = []
        for l in s :
            if l in lst : return l
            else : lst.append(l)
        return ""