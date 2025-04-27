## https://leetcode.com/problems/maximum-height-of-a-triangle/

class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        s1, s2, ans, m1, m2 = 1, 2, 2, min(red, blue), max(red, blue)
        while True :
            if s1 == m1:
                if s2 <= m2: return ans
                else: return ans - 1
            elif s2 == m1:
                if s1 + ans + 1 <= m2: return ans + 1
                else: return ans
            elif s1 > m1 and s2 - ans <= m1:
                if s1 <= m2: return ans - 1
                else: return ans - 2
            elif s1 - (ans - 1) <= m1 and s2 - ans > m1:
                if s2 - ans <= m2: return ans - 2
                else: return ans - 3
            s1 += ans + 1
            s2 += ans + 2
            ans += 2