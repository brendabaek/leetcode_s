## https://leetcode.com/problems/substring-matching-pattern/

class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        l = p.split("*")
        if l[0] in s: s = s[s.index(l[0]) + len(l[0]):]
        else: return False
        return True if l[1] in s else False

        # p1, p2 = p[:p.index("*")], p[p.index("*")+1:]
        # try: s = s[s.index(p1) + len(p1):]
        # except: return False
        # return True if p2 in s else False