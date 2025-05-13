## https://leetcode.com/problems/find-the-largest-almost-missing-integer/

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        if k == 1:
            for n in sorted(list(set(nums)), reverse = True):
                if nums.count(n) == 1: return n
            return -1
        elif k == len(nums): return max(nums)
        m1, m2 = max(nums[0], nums[-1]), min(nums[0], nums[-1])
        if nums.count(m1) == 1: return m1
        elif nums.count(m2) == 1: return m2
        else: return -1