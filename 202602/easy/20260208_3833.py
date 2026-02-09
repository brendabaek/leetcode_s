## https://leetcode.com/problems/count-dominant-indices/

class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        s, ln, ans = sum(nums), len(nums), 0
        while ln > 1:
            n = nums.pop(0)
            s, ln = s - n, ln - 1
            if n > s / ln: ans += 1
        return ans