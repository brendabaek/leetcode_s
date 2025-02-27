## https://leetcode.com/problems/calculate-amount-paid-in-taxes/

class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        p, ans = 0, 0
        for b in brackets :
            if b[0] > income : return ans + max((income - p) * b[1] / 100, 0)
            else : ans += (b[0]-p) * b[1] / 100
            p = b[0]
        return ans