## https://leetcode.com/problems/maximize-expression-of-three-elements/

class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        ans = max(nums)
        nums.pop(nums.index(ans))
        return ans + max(nums) - min(nums)