## https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return True if sorted(target) == sorted(arr) else False