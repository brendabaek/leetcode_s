## https://leetcode.com/problems/strong-password-checker-ii/

class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        c2, c3, c4, c5, pre, sc = False, False, False, False, "", "!@#$%^&*()-+"
        if len(password) < 8 : return False
        for p in password :
            if p == pre : return False
            n = ord(p)
            if c2 == True : pass
            else :
                if 97 <= n and n <= 122 : c2 = True
            if c3 == True : pass
            else :
                if 65 <= n and n <= 90 : c3 = True
            if c4 == True : pass
            else :
                if 48 <= n and n <= 57 : c4 = True
            if c5 == True : pass
            else :
                if p in sc : c5 = True
            pre = p
        return True if c2 == c3 == c4 == c5 == True else False