## https://leetcode.com/problems/sort-colors/

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        check = set(nums)
        if len(check) == 1 : return nums
        elif len(check) == 2 :
            idx = 1
            while idx < len(nums) :
                if nums[idx] >= nums[idx-1] : idx += 1
                else : nums.insert(0, nums.pop(idx))
            return nums

        else : ## len(check) == 3
            idx, cnt = 1, 0
            while idx < len(nums) :
                if nums[idx] == 1 : nums.pop(idx); cnt += 1
                elif nums[idx] >= nums[idx-1] : idx += 1
                else : nums.insert(0, nums.pop(idx))
            point = nums.index(2)
            for i in range(cnt) : nums.insert(point, 1)
            return nums
