## https://leetcode.com/problems/number-of-bit-changes-to-make-two-integers-equal/

class Solution:
    def minChanges(self, n: int, k: int) -> int:
        if n == k: return 0
        b1, b2, ans = bin(n)[2:][::-1], bin(k)[2:][::-1], 0
        ln1, ln2 = len(b1), len(b2)
        if ln2 > ln1: return -1
        for i in range(ln2):
            if b1[i] == "1" and b2[i] == "0": ans += 1
            elif b1[i] == "0" and b2[i] == "1": return -1
        return ans + b1[ln2:].count("1")