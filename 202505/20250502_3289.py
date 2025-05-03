## https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        p, ans = nums[0], []
        for i in range(1, len(nums)):
            if p == nums[i]:
                ans.append(p)
                if len(ans) == 2: return ans
            p = nums[i]
        return ans