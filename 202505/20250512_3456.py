## https://leetcode.com/problems/find-special-substring-of-length-k/

class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        ln = len(s)
        for i in range(ln - k + 1):
            if len(set(s[i:i+k])) == 1:
                if i == 0 and i + k >= ln: return True
                elif i == 0 and s[i + k - 1] != s[i + k]: return True
                elif i != 0 and s[i - 1] != s[i] and i + k >= ln: return True
                elif i != 0 and s[i - 1] != s[i] and s[i + k - 1] != s[i + k]: return True
        return False