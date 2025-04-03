## https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-i/

class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        if set(s1) != set(s2) : return False
        s1, s2 = list(s1), list(s2)
        for i in range(2) :
            if s1[i] != s2[i] :
                if s1[i] == s2[i+2] : s2[i], s2[i+2] = s2[i+2], s2[i]
                else : return False
        return s1 == s2