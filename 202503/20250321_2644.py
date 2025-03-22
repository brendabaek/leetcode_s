## https://leetcode.com/problems/find-the-maximum-divisibility-score/

class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        cnt, ans = 0, 0
        for d in divisors :
            c = 0
            for num in nums :
                if num % d == 0 : c += 1
            if c == cnt : ans = min(ans, d)
            elif c > cnt : cnt, ans = c, d
        return ans if ans != 0 else min(divisors)