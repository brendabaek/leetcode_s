## https://leetcode.com/problems/semi-ordered-permutation/

class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        ln = len(nums)
        ans = nums.index(1)
        if nums.index(ln) > ans : ans += ln - 1 - nums.index(ln)
        else : ans += ln - 2 - nums.index(ln)
        return ans