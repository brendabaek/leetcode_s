## https://leetcode.com/problems/jump-game-ii/

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx, ans, ln = 0, 0, len(nums)
        while idx < ln-1 :
            if idx + nums[idx] >= ln-1 : return ans+1
            cand = nums[idx+1:idx+1+nums[idx]]
            tmp = 1
            for i in range(len(cand)) :
                if tmp <= (i + 1 + cand[i]) :
                    cnt = i+1
                    tmp = i+1 + cand[i]
            idx += cnt
            ans += 1
        return ans
    
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sums = [nums[i]+i for i in range(len(nums))]
        tmp, idx, ans = 0, 0, 0
        while tmp < len(nums)-1 :
            ans += 1
            idx, tmp = tmp+1, max(sums[idx:tmp+1])
        return ans