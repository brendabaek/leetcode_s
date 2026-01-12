## https://leetcode.com/problems/minimum-number-of-flips-to-reverse-binary-string/

class Solution:
    def minimumFlips(self, n: int) -> int:
        s, ans = bin(n)[2:], 0
        for i in range(len(s)):
            if s[i] != s[-i-1]: ans += 1
        return ans