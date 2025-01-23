## https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        p, ans = 0, 0
        for n in nums :
            if n <= p :
                ans += p - n + 1
                p = p + 1
            else : p = n
        return ans