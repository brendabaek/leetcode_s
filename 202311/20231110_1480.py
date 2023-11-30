## https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sums, ans = 0, []
        for n in nums :
            sums += n
            ans.append(sums)
        return ans