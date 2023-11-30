## https://leetcode.com/problems/reformat-the-string/

class Solution:
    def reformat(self, s: str) -> str:
        c, n, ans = [], [], ""
        for l in s :
            if l.isalpha() : c.append(l)
            else : n.append(l)
        ln, ln_c, ln_n = len(s), len(c), len(n)

        if abs(ln_c - ln_n) > 1 : return ""
        
        for _ in range(ln//2) :
            ans += n.pop() + c.pop()
        try : ans += n.pop()
        except :
            try : ans = c.pop() + ans
            except : return ans
        return ans