## https://leetcode.com/problems/subsets/

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        tmp, ans = [], [[]]
        for i in range(1, len(nums)+1) :
            tmp, ans = self.make_answer(nums, i, i, tmp, ans)
        return ans
    
    def make_answer(self, nums, cnt, point, tmp, ans) :
        for i in range(len(nums)-point+1) :
            tmp.append(nums[i])
            if len(tmp) == cnt : ans.append(tmp[:])
            else : tmp, ans = self.make_answer(nums[i+1:], cnt, point-1, tmp, ans)
            try : tmp.pop()
            except : pass
        return tmp, ans