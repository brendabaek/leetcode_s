## https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

class Solution:
    def check(self, nums: List[int]) -> bool:
        if len(nums) < 3 : return True
        if nums[0] > nums[1] : ans, c = True, nums[1]
        else : ans, c = True, nums[0]
        for n in nums[1:]+nums[:2] :
            if n >= c : c = n
            else :
                if ans : ans, c = False, n
                else : return ans
        return True