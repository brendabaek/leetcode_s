## https://leetcode.com/problems/minimum-cost-to-reach-every-position/

class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        ans, t = [], 100
        for c in cost:
            if c < t: t = c
            ans.append(t)
        return ans