## https://leetcode.com/problems/maximize-pair-strength-using-gcd/

class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        nums = sorted(set(nums), reverse = True)
        ln, ans = len(nums), 1
        for i in range(ln - 1):
            if nums[i] * nums[i + 1] <= ans: return ans
            for j in range(i + 1, ln):
                if nums[i] * nums[j] <= ans: break
                ans = max(ans, nums[i] * nums[j] // gcd(nums[i], nums[j]) ** 2)
        return ans