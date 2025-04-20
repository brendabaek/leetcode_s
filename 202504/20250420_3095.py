## https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-i/

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        if max(nums) >= k: return 1
        ln = len(nums)
        for i in range(2, ln+1):
            for j in range(ln-i+1):
                lst, o = nums[j:j+i], 0
                for l in lst: o |= l
                if o >= k: return len(lst)
        return -1