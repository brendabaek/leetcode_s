## https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n, ln = sorted(nums), len(nums)
        ans = [0] * ln
        for i in range(ln) : ans[i] = n.index(nums[i])
        return ans