## https://leetcode.com/problems/count-square-sum-triples/

class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0
        for i in range(1, n) :
            for j in range(1, i) :
                k = (i*i + j*j) ** (0.5)
                if k > n : break
                if int(k) == k : ans += 2
        return ans