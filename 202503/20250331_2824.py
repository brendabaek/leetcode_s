## https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        ln, ans = len(nums), 0
        for i in range(ln-1) :
            t = target - nums[i]
            for j in range(i+1, ln) :
                if nums[j] < t : ans += 1
        return ans