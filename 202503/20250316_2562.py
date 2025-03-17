## https://leetcode.com/problems/find-the-array-concatenation-value/

class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        ans = 0
        while len(nums) > 1 :
            n1, n2, d = nums.pop(0), nums.pop(), 10
            while n2 // d > 0 : d *= 10
            ans += (n1 * d) + n2
        return ans + sum(nums)