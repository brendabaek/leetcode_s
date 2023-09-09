## https://leetcode.com/problems/subsets-ii/

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = [[]]
        for i in range(len(nums)) :
            if i == 0 or nums[i-1] != nums[i] :
                ans = self.make_answer(nums[i:], [], ans)
        return ans

    def make_answer(self, nums, tmp, ans) :
        tmp.append(nums[0])
        if tmp not in ans : ans.append(tmp[:])
        for i in range(1, len(nums)) :
            ans = self.make_answer(nums[i:], tmp[:], ans)
        return ans