## https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # s_nums = set(nums)
        # for num in s_nums :
        #     if nums.count(num) != 1 : return num
        # nums.sort()
        # idx, ln = 0, len(nums)
        # while idx < ln-1 :
        #     if nums[idx] == nums[idx+1] : return nums[idx]
        #     else : idx += 1
        dics = {}
        for num in nums :
            try :
                dics[num] += 1
                return num
            except : dics[num] = 1