## https://leetcode.com/problems/single-number/

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1 : return nums[0]
        nums.sort()
        return self.find_nums(nums)[0]

    def find_nums(self, nums) :
        ln = len(nums)
        if ln == 1 : return nums

        i = (ln // 4) * 2
        if nums[i] == nums[i+1] :
            return self.find_nums(nums[i+2:])
        
        else :
            return self.find_nums(nums[:i+1])