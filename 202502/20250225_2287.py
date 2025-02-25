## https://leetcode.com/problems/rearrange-characters-to-make-target-string/

class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        s, ans = list(s), 0
        while True :
            for t in target :
                try : s.remove(t)
                except : return ans
            ans += 1
        return ans