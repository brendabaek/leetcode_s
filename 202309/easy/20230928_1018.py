## https://leetcode.com/problems/binary-prefix-divisible-by-5/

class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        ans, num = [], 0
        for i in range(len(nums)) :
            num = (num * 2) + nums[i]
            ans.append(num % 5 == 0)
        return ans