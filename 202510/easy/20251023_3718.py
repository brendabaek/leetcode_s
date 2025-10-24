## https://leetcode.com/problems/smallest-missing-multiple-of-k/

class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums.sort()
        c = k
        while True:
            if nums == [] or nums[-1] < c: return c
            for i in range(len(nums)):
                if nums[i] > c: return c
                elif nums[i] == c:
                    nums = nums[i+1:]
                    c += k
                    break