## https://leetcode.com/problems/find-the-key-of-the-numbers/

class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        i, ans = 0, 0
        for _ in range(4):
            ans += min(num1 % 10, num2 % 10, num3 % 10) * (10 ** i)
            i, num1, num2, num3 = i + 1, num1 // 10, num2 // 10, num3 // 10
        return ans