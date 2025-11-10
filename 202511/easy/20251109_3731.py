## https://leetcode.com/problems/find-missing-elements/

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        s, ans = nums[0], []
        for n in nums:
            if s < n:
                while s < n:
                    ans.append(s)
                    s += 1
            s += 1               
        return ans