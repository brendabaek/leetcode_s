## https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/

class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        n1, n2, n3, ans = 0, nums[0], nums[1], 0
        for num in nums[2:]:
            n1, n2, n3 = n2, n3, num
            if (n1 + n3) * 2 == n2: ans += 1
        return ans