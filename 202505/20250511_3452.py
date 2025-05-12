## https://leetcode.com/problems/sum-of-good-numbers/

class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        ln, ans = len(nums), 0
        for i in range(ln):
            if i - k >= 0 and nums[i] <= nums[i - k]: continue
            if i + k < ln and nums[i] <= nums[i + k]: continue
            ans += nums[i]
        return ans