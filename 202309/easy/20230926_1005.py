## https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/

class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()

        for i in range(len(nums)) :
            if k == 0 : break
            if nums[i] < 0 :
                nums[i] = -nums[i]
                k -= 1
            elif nums[i] == 0 :
                k = 0
                break
            else : break

        if k % 2 == 0 : return sum(nums)
        else : return sum(nums) - (min(nums) * 2)