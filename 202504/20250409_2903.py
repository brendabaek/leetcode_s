## https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/

class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        ln = len(nums)
        for i in range(ln - indexDifference) :
            f = nums[i]
            for j in range(i + indexDifference, ln) :
                if abs(f - nums[j]) >= valueDifference : return [i, j]
        return [-1, -1]