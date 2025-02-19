## https://leetcode.com/problems/count-hills-and-valleys-in-an-array/

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        if len(nums) < 3 : return 0
        s, p, e, ln, ans = 0, 1, 2, len(nums), 0
        while e < ln :
            while nums[s] == nums[p] or nums[p] == nums[e] :
                if e == ln-1 : break
                while nums[s] == nums[p] and p < ln-2 : s, p, e = s+1, p+1, p+2
                while nums[p] == nums[e] and e < ln-1 : p, e = p+1, e+1
            if nums[s] < nums[p] and nums[e] < nums[p] : ans += 1
            elif nums[s] > nums[p] and nums[e] > nums[p] : ans += 1
            while nums[s] == nums[s+1] and s < ln-3 : s += 1
            s, p, e = s+1, max(s+2, p), max(s+3, p+1, e)
        return ans