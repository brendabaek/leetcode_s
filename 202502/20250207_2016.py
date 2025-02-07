## https://leetcode.com/problems/maximum-difference-between-increasing-elements/

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        c, n, ln, ans = 0, 0, len(nums), -1
        while n < ln :
            for i in range(n+1, ln) :
                if nums[i] > nums[n] : ans = max(ans, nums[i]-nums[n])
                elif nums[i] < nums[n] : n = i
            if n == c : return ans
            else : c = n
        return ans