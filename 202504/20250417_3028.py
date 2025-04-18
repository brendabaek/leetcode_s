## https://leetcode.com/problems/ant-on-the-boundary/

class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        s, ans = 0, 0
        for num in nums:
            s += num
            if s == 0: ans += 1
        return ans