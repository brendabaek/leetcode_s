## https://leetcode.com/problems/number-of-arithmetic-triplets/

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        ans = 0
        for n in nums :
            if n+diff in nums and n+diff+diff in nums : ans += 1
        return ans