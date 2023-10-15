## https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        check, ans = 0, 0
        for l in s :
            if l == "R" : check += 1
            else : check -= 1
            if check == 0 : ans += 1
        return ans