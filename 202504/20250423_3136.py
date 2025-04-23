## https://leetcode.com/problems/valid-word/

class Solution:
    def isValid(self, word: str) -> bool:
        l1 = "aeiouAEIOU"
        l2 = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
        l3 = "0123456789"
        c1, c2 = False, False
        if len(word) < 3: return False
        for w in word:
            if w not in l1 + l2 + l3: return False
            if w in l1: c1 = True
            elif w in l2: c2 = True
        return True if c1 == True and c2 == True else False 