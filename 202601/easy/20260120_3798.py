## https://leetcode.com/problems/largest-even-number/

class Solution:
    def largestEven(self, s: str) -> str:
        while True:
            if s == "" or s[-1] == "2": return s
            else: s = s[:-1]
        return s