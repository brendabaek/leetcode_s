## https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        ans = True
        for i in range(len(s1)) :
            if s1[i] != s2[i]:
                if ans == True : ans, idx = False, i
                else :
                    if s1 == s2[:idx] + s2[i] + s2[idx+1:i] + s2[idx] + s2[i+1:] : return True
                    else : return False
        return ans