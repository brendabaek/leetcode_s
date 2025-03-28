## https://leetcode.com/problems/longest-even-odd-subarray-with-threshold/

class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        ln, ans = len(nums), 0
        for i in range(ln) :
            s = nums[i]
            if s > threshold or s % 2 == 1 : continue
            cnt = 1
            for j in range(i+1, ln) :
                e = nums[j]
                if e > threshold or (s + e) % 2 == 0 : break
                else : cnt += 1; s = e
            ans = max(ans, cnt)
        return ans