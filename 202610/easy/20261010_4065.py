## https://leetcode.com/problems/rearrange-array-by-removing-distinct-values/

class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        ans = []
        while nums:
            s = sorted(list(set(nums)))
            ans += s
            for n in s: nums.remove(n)
        return ans