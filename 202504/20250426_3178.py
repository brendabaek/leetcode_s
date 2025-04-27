## https://leetcode.com/problems/find-the-child-who-has-the-ball-after-k-seconds/

class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        if (k // (n - 1)) % 2 == 0: return k % (n - 1)
        else: return (n - 1) - (k % (n - 1))