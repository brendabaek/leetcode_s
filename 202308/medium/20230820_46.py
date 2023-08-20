## https://leetcode.com/problems/permutations/

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.make_answer(nums, [], [])

    def make_answer(self, nums, tmp, ans) :
        for i in range(len(nums)) :
            nums2, tmp2 = nums[:], tmp[:]
            tmp2.append(nums2.pop(i))
            if len(nums2) == 0 :
                ans.append(tmp2)
                return ans
            ans = self.make_answer(nums2, tmp2, ans)
        return ans