## https://leetcode.com/problems/minimum-number-of-chairs-in-a-waiting-room/

class Solution:
    def minimumChairs(self, s: str) -> int:
        tmp, ans = 0, 0
        for l in s:
            if l == "E": tmp += 1; ans = max(ans, tmp)
            else: tmp -= 1
        return ans