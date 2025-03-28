## https://leetcode.com/problems/longest-alternating-subarray/

class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        idx, ans, ln = 0, -1, len(nums)
        while idx < ln - 1 :
            if nums[idx] + 1 != nums[idx+1] : idx += 1; continue
            sample = nums[idx:idx+2]
            cnt, idx = 2, idx + 2
            while idx < ln :
                if nums[idx:idx+2] == sample : cnt += 2; idx += 2
                elif nums[idx] == sample[0] : cnt += 1; idx += 1; break
                else : idx -= 1; break
            ans = max(ans, cnt)
        return ans