## https://leetcode.com/problems/valid-elements-in-an-array/

class Solution:
    def findValidElements(self, nums: list[int]) -> list[int]:
        if len(nums) <= 2: return nums
        ans, m1 = [], 0
        for i in range(len(nums) - 1):
            if nums[i] > m1:
                m1 = nums[i]
                ans.append(nums[i])
            else:
                try: m2 = max(nums[i+1:])
                except: return ans[:i] + nums[-1:]
                if nums[i] > m2: ans.append(nums[i])
        return ans + nums[-1:]