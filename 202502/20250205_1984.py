## https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1 : return 0
        nums.sort()
        ans = 100000
        for i in range(len(nums)-k+1) :
            ans = min(ans, nums[i+k-1] - nums[i])
        return ans