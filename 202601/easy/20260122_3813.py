## https://leetcode.com/problems/vowel-consonant-score/

class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        c, v = 0, 0
        for l in s:
            if l in "aeiou": v += 1
            elif l.isalpha(): c += 1
        return 0 if c == 0 else v // c