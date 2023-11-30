## https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/

class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        tot, sums, cnt = sum(nums), 0, 0
        for n in nums :
            sums += n
            tot -= n
            cnt += 1
            if sums > tot : return nums[:cnt]
        return nums