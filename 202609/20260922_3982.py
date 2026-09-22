## https://leetcode.com/problems/sum-of-integers-with-maximum-digit-range/

class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        k, v = 0, 0
        for num in nums:
            n = list(str(num))
            r = int(max(n)) - int(min(n))
            if r > k: k, v = r, num
            elif r == k: v += num
        return v