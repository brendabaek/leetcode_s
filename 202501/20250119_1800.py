## https://leetcode.com/problems/maximum-ascending-subarray-sum/

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans, sums, p = 0, 0, 0
        for n in nums :
            if p < n :
                sums += n
            else :
                ans = max(ans, sums)
                sums = n
            p = n
        return max(ans, sums)