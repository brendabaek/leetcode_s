## https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter/

class Solution:
    def minTimeToType(self, word: str) -> int:
        p, ans = 97, 0
        for w in word :
            ans += min(abs(p-ord(w)), 26-abs(p-ord(w))) + 1
            p = ord(w)
        return ans