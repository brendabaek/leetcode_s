## https://leetcode.com/problems/find-the-middle-index-in-array/

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        ln = len(nums)
        l, m, r = 0, nums[0], sum(nums[1:])
        if l == r : return 0
        for i in range(1, ln) :
            l, m, r = l + nums[i-1], nums[i], r - nums[i]
            if l == r : return i
        return -1