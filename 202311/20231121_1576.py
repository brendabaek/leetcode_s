## https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/

class Solution:
    def modifyString(self, s: str) -> str:
        ln, u = len(s), 97
        for i in range(ln) :
            if s[i] != "?" : continue
            else :
                if i == ln-1 :
                    while ord(s[i-1]) == u :
                        if u == 122 : u = 97
                        else : u += 1
                else :
                    while ord(s[i-1]) == u or ord(s[i+1]) == u :
                        if u == 122 : u = 97
                        else : u += 1
                s = s[:i] + chr(u) + s[i+1:]
        return s
