## https://leetcode.com/problems/lexicographically-smallest-palindrome/

class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s, ln = list(s), len(s)
        for i in range(ln // 2 + 1) :
            f, e = s[i], s[ln-1-i]
            if f == e : continue
            elif f > e : s[i] = e
            else : s[ln-1-i] = f
        return "".join(s)