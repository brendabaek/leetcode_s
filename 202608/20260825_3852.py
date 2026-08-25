## https://leetcode.com/problems/smallest-pair-with-different-frequencies/

class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        nums.sort()
        num1 = nums[0]
        m = nums.count(nums[0])
        if nums[m:] == []: return [-1, -1]
        else: n, cnt = nums[m], 0
        for num in nums[m:]:
            if num == n: cnt += 1
            else:
                if cnt == m:n, cnt = num, 1
                else: return [num1, n]
        if m == cnt: return [-1, -1]
        else: return [num1, num]