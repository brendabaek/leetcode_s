## https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        sums, mins = 0, 100
        for num in nums :
            sums += num
            mins = min(mins, sums)
        return -mins + 1 if mins < 0 else 1