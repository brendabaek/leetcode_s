## https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx, cnt, num = 1, 1, nums[0]
        while idx < len(nums) :
            if nums[idx] == num :
                cnt += 1
                if cnt > 2 : nums.pop(idx)
                else : idx += 1
            else :
                cnt, num = 1, nums[idx]
                idx += 1
        return len(nums)
