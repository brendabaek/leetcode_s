## https://leetcode.com/problems/decompress-run-length-encoded-list/

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ln, ans = len(nums)//2, []
        for i in range(ln) :
            ans += [nums[i*2+1]] * nums[i*2]
        return ans