## https://leetcode.com/problems/minimum-distance-between-three-equal-elements-i/

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        dics, ans = {}, len(nums)
        for i in range(len(nums)):
            try: dics[nums[i]].append(i)
            except: dics[nums[i]] = [i]
        for k, v in dics.items():
            v.sort()
            if len(v) >= 3:
                for i in range(2, len(v)):
                    if v[i] - v[i-2] < ans: ans = v[i] - v[i-2]
        return ans * 2 if ans != len(nums) else -1