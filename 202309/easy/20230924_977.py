## https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for num in nums : ans.append(num*num)
        if nums[0] >= 0 : return ans
        elif nums[-1] <= 0 : ans.reverse()
        else : ans.sort()
        return ans