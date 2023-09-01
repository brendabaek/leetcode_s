## https://leetcode.com/problems/permutations-ii/

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.make_answer(nums, [], set())

    def make_answer(self, nums, tmp, ans) :
        for i in range(len(nums)) :
            tmp2, nums2 = tmp[:], nums[:]
            tmp2.append(nums2.pop(i))
            if len(nums2) == 0 :
                ans.add(tuple(tmp2))
                return ans
            ans = self.make_answer(nums2, tmp2, ans)
        return ans