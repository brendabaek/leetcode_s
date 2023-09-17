## https://leetcode.com/problems/sort-array-by-parity/

class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        idx, cnt, ln = 0, 0, len(nums)
        while cnt < ln :
            if nums[idx] % 2 == 1 : nums.append(nums.pop(idx))
            else : idx += 1
            cnt += 1
        return nums