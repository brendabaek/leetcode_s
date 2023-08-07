## https://leetcode.com/problems/third-maximum-number/

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        ans = []
        
        for num in nums :
            if len(ans) < 3 :
                ans.append(num)
            else :
                ans.append(num)
                ans.remove(min(ans))

        if len(ans) < 3 : return max(ans)
        else : return min(ans)