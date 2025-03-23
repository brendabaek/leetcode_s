## https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/

class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        # return sum(max(nums) + n for n in range(k))

        # ans = 0
        # for i in range(max(nums), max(nums)+k) : ans += i
        # return ans

        n = max(nums)
        return k * ((2 * n) + (k - 1)) // 2