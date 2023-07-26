## https://leetcode.com/problems/missing-number/

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        mn = 0
        mx = len(nums)+1
        md = mx // 2
        if nums[0] != 0 : return mn
        while (mx-mn) != 1 :
            try :
                if nums[md] == md : mn = md
                else : mx = md
                md = (mn + mx) // 2
            except : return mx-1
        return mx