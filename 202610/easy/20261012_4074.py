## https://leetcode.com/problems/maximum-product-pair-with-target-sum/

class Solution:
    def maxProductPair(self, nums: list[int], target: int) -> list[int]:
        new, n, p = sorted(set(nums)), None, -10001
        if len(new) < 2 or new[-1] + new[-2] < target: return [-1, -1]
        for i in range(len(new)-1, 0, -1):
            if new[i] * 2 <= target : break
            if target - new[i] in new[:i] and new[i] * (target - new[i]) > p: n = new[i]
        return [nums.index(n), nums.index(target - n)] if n != None else [-1, -1]