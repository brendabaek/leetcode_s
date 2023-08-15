## https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ln = len(nums)
        ans = []
        for i in range(ln) :
            if nums[i] == target and len(ans) == 0 :ans.append(i)
            if nums[i] == target and i == ln-1 : ans.append(i)
            if nums[i-1] == target and nums[i] != target and len(ans) == 1 :
                ans.append(i-1)
                return ans
        if ans == [] : return [-1, -1]
        return ans