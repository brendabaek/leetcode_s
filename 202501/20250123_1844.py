## https://leetcode.com/problems/replace-all-digits-with-characters/

class Solution:
    def replaceDigits(self, s: str) -> str:
        def shift(a, b) : return int(ord(a)) + int(b)
        for i in range(len(s)//2) :
            s = s[:2*i+1] + chr(shift(s[2*i], s[2*i+1])) + s[2*i+2:]
        return s