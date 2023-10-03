## https://leetcode.com/problems/height-checker/

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        new_h, ans = sorted(heights), 0
        for i in range(len(heights)) :
            if heights[i] != new_h[i] : ans += 1
        return ans