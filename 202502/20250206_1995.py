## https://leetcode.com/problems/count-special-quadruplets/

class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        ln = len(nums)
        ans = 0
        for i in range(ln-3) :
            for j in range(i+1, ln-2) :
                for k in range(j+1, ln-1) :
                    n = nums[i] + nums[j] + nums[k]
                    ans += nums[k+1:].count(n)
        return ans