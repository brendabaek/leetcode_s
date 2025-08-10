## https://leetcode.com/problems/hexadecimal-and-hexatrigesimal-conversion/

class Solution:
    def concatHex36(self, n: int) -> str:
        ans1 = hex(n*n).upper()[2:]
        ans2 = ""
        l = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        n = n * n * n
        while n > 0:
            ans2 = l[n % 36] + ans2
            n //= 36
        return ans1 + ans2