## https://leetcode.com/problems/compute-alternating-sum/

class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        ans, check = 0, True
        for num in nums:
            if check: ans += num; check = False
            else: ans -= num; check = True
        return ans