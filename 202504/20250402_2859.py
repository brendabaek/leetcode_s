## https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/

class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        ln, ans = len(nums), 0
        for i in range(ln) :
            if bin(i).count("1") == k : ans += nums[i]
        return ans