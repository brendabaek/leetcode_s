## https://leetcode.com/problems/check-ascii-palindromic/

class Solution:
    def isPalindromic(self, s: str) -> bool:
        ln, i= (len(s) + 1) // 2, 0
        while i < ln:
            if bin(ord(s[i]))[2:].rjust(8, '0') != bin(ord(s[-i-1]))[2:].rjust(8, '0')[::-1]: return False
            i += 1
        return True