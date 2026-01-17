## https://leetcode.com/problems/absolute-difference-between-maximum-and-minimum-k-elements/

class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0
        return sum(nums[-k:]) - sum(nums[:k])
        # for i in range(k): ans += nums[-i-1] - nums[i]
        # return ans