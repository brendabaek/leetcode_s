## https://leetcode.com/problems/trim-trailing-vowels/

class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        while s != "":
            if s[-1] in 'aeiou': s = s[:-1]
            else: return s
        return s