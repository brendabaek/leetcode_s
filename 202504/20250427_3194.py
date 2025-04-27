## https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/

class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        ans = []
        while nums != []: ans.append((nums.pop(0) + nums.pop()) / 2)
        return min(ans)