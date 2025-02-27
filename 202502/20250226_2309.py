## https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/

class Solution:
    def greatestLetter(self, s: str) -> str:
        for i in range(25, -1, -1) :
            u, l = chr(i + 65), chr(i + 97)
            if u in s and l in s : return u
        return ""