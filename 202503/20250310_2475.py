## https://leetcode.com/problems/number-of-unequal-triplets-in-array/

class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        idx1, idx2, idx3, ln, ans = 0, 1, 2, len(nums), 0
        while idx1 < ln - 2 :
            while idx2 < ln - 1 :
                while idx3 < ln :
                    if nums[idx1] != nums[idx2] and nums[idx2] != nums[idx3] and nums[idx1] != nums[idx3] : ans += 1
                    idx3 += 1
                idx2, idx3 = idx2 + 1, idx2 + 2
            idx1, idx2, idx3 = idx1 + 1, idx1 + 2, idx1 + 3
        return ans