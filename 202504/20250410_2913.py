## https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans, ln = 0, len(nums)
        for i in range(ln) :
            s = set([nums[i]])
            ans += 1
            for j in range(i+1, ln) :
                s.add(nums[j])
                ans += len(s) ** 2
        return ans