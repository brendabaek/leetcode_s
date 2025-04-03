## https://leetcode.com/problems/points-that-intersect-with-cars/

class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        # nums.sort()
        # idx, ans, s, e = 1, nums[0][1] - nums[0][0] + 1, nums[0][0], nums[0][1]
        # while idx < len(nums) :
        #     if nums[idx][0] <= e : ans += max(0, nums[idx][1] - e); e = max(e, nums[idx][1])
        #     else : ans += nums[idx][1] - nums[idx][0] + 1; s, e = nums[idx][0], nums[idx][1]
        #     idx += 1
        # return ans

        nums.sort()
        idx, ans = 1, 0
        while idx < len(nums) :
            if nums[idx][0] <= nums[idx-1][1] :
                nums[idx-1][1] = max(nums[idx-1][1], nums[idx][1])
                nums.pop(idx)
            else : idx += 1
        for num in nums : ans += num[1] - num[0] + 1
        return ans