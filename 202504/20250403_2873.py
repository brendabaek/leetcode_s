## https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-i/

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        p, ans = 0, 0
        for k in range(len(nums)-1, 1, -1) :
            if nums[k] > p :
                p, t, m = nums[k], 0, 0
                for i in range(k-1) :
                    if nums[i] > m :
                        m = nums[i]
                        t = max(t, m - min(nums[i+1:k]))
                ans = max(ans, t * p)
        return ans