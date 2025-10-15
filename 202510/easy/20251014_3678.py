## https://leetcode.com/problems/smallest-absent-positive-greater-than-average/

class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        n = sum(nums) / len(nums)
        if n <= 0: n = 1
        elif round(n) <= n: n = int(round(n) + 1)
        else: n = int(round(n))
        while True:
            if n in nums: n += 1
            else: return n