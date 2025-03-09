## https://leetcode.com/problems/number-of-distinct-averages/

class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        s = set()
        while nums != [] :
            a, b = max(nums), min(nums)
            s.add((a+b)/2)
            nums.remove(a), nums.remove(b)
        return len(s)