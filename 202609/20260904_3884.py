## https://leetcode.com/problems/first-matching-character-from-both-ends/

class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        f, e = 0, len(s)-1
        while f <= e:
            if s[f] == s[e]: return f
            f, e = f + 1, e - 1
        return -1