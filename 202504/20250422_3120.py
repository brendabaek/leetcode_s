## https://leetcode.com/problems/count-the-number-of-special-characters-i/

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        word, ans = set(word), 0
        for w in word:
            n = ord(w)
            if 65 <= n and n <= 90 and chr(n+32) in word: ans += 1
        return ans