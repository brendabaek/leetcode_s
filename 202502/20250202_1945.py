## https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        n = ""
        for i in s : n += str(ord(i)-96)
        n = int(n)
        while k > 0 :
            tmp = 0
            while n > 0 : tmp, n = tmp + n % 10, n // 10
            n, k = tmp, k-1
        return n