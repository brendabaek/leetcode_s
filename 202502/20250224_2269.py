## https://leetcode.com/problems/find-the-k-beauty-of-a-number/

class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        new, n, ans = num // (10 ** k), num % (10 ** k), 0        
        while new > 0 :
            if n == 0 : pass
            elif num % n == 0 : ans += 1
            n = n + ((new % 10) * (10 ** k))
            n, new = n // 10, new // 10
        if n == 0 : return ans
        if num % n == 0 : return ans + 1
        return ans