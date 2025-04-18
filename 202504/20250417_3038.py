## https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-i/

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        s, ans = sum(nums[:2]), 1
        for i in range(2, len(nums), 2):
            try:
                if nums[i] + nums[i+1] == s: ans += 1
                else: break
            except: break
        return ans