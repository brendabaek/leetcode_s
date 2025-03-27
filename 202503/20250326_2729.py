## https://leetcode.com/problems/check-if-the-number-is-fascinating/

class Solution:
    def isFascinating(self, n: int) -> bool:
        if n > 333 : return False
        ans = set([0])
        for i in [n, n*2, n*3] :
            while i > 0 :
                if i % 10 in ans : return False
                else : ans.add(i % 10)
                i //= 10
        return len(ans) == 10