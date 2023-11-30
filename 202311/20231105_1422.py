## https://leetcode.com/problems/maximum-score-after-splitting-a-string/

class Solution:
    def maxScore(self, s: str) -> int:
        ln, sums, ans = len(s), s.count("1"), 0
        for l in s[:-1] :
            if l == "0" : sums += 1
            else : sums -= 1
            ans = max(ans, sums)
        return ans