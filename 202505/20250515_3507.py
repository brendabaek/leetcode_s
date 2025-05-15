## https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ans = 0
        while True:
            p, check = nums[0], True
            for n in nums[1:]:
                if n < p:
                    s, idx = sum(nums[:2]), 0
                    for i in range(len(nums) - 1):
                        if sum(nums[i:i+2]) < s: s, idx = sum(nums[i:i+2]), i
                    nums[idx] = s; nums.pop(idx+1); ans += 1; check = False; break
                p = n
            if check == True: return ans