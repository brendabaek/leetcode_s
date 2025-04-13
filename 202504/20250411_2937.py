## https://leetcode.com/problems/make-three-strings-equal/

class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        ln1, ln2, ln3 = len(s1), len(s2), len(s3)
        for i in range(min(ln1, ln2, ln3)):
            if s1[i] != s2[i] or s2[i] != s3[i] or s1[i] != s3[i]: idx = i; break
        try:
            if idx == 0 : return -1
        except: idx = min(ln1, ln2, ln3)
        return ln1 + ln2 + ln3 - idx * 3