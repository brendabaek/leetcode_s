## https://leetcode.com/problems/set-mismatch/

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        cnt, fst, lst = 0, 0, 0
        while cnt < len(nums) -1 :
            if nums[cnt] == nums [cnt+1] :
                fst = nums[cnt]
            if nums[cnt] + 2 == nums[cnt+1] :
                lst = nums[cnt] +1
            cnt += 1

        if nums[0] != 1 : lst = 1
        elif nums[-1] != len(nums) : lst = len(nums)
        return [fst, lst]