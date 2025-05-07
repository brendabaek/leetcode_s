## https://leetcode.com/problems/transformed-array/

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        ln, ans = len(nums), []
        for i in range(ln): ans.append(nums[(i + nums[i]) % ln])
        return ans