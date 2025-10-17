## https://leetcode.com/problems/bitwise-or-of-even-numbers-in-an-array/

class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        ans = 0
        for n in nums:
            if n % 2 == 0: ans |= n
        return ans