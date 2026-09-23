## https://leetcode.com/problems/number-of-elapsed-seconds-between-two-times/

class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        s, e, ans = startTime.split(":"), endTime.split(":"), 0
        for i in range(3): ans += (int(e[i]) - int(s[i])) * 60 ** (2 - i)
        return ans