## https://leetcode.com/problems/consecutive-characters/

class Solution:
    def maxPower(self, s: str) -> int:
        ln, tmp, ans = len(s), 1, 1
        for i in range(1, ln) :
            if s[i-1] == s[i] :
                tmp += 1
                ans = max(tmp, ans)
            else : tmp = 1
        return ans