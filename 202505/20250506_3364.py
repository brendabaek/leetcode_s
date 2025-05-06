## https://leetcode.com/problems/minimum-positive-sum-subarray/

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        ln = len(nums)
        ans = sum(nums[:l]) if sum(nums[:l]) > 0 else 100001
        for i in range(l, r+1):
            idx, s = 0, sum(nums[:i])
            if s == 1: return 1
            elif s > 1 and s < ans: ans = s
            while idx < ln - i:
                s = s - nums[idx] + nums[idx + i]
                if s == 1: return 1
                elif s > 1 and s < ans: ans = s
                idx += 1
        return ans if ans < 100001 else -1