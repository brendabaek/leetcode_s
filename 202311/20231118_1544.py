## https://leetcode.com/problems/make-the-string-great/

class Solution:
    def makeGood(self, s: str) -> str:
        while len(s) > 0 :
            ln, check = len(s), True
            for i in range(ln-1) :
                if abs(int(ord(s[i]))-int(ord(s[i+1]))) == 32 :
                    s = s[:i] + s[i+2:]
                    check = False
                    break
            if check == True : return s
        return s