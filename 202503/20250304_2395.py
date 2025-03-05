## https://leetcode.com/problems/find-subarrays-with-equal-sum/

class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        s, sums = nums[0], []
        for num in nums[1:] :
            sums.append(s+num)
            s = num
        return False if len(sums) == len(set(sums)) or len(sums) < 2 else True