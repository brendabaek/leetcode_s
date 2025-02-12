## https://leetcode.com/problems/find-target-indices-after-sorting-array/

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        idx, ans = 0, []
        while idx < len(nums) :
            if nums[idx] > target : break
            if nums[idx] == target : ans.append(idx)
            idx += 1
        return ans