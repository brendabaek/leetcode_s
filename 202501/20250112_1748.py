## https://leetcode.com/problems/sum-of-unique-elements/

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        nums.sort()
        try :
            if nums[0] != nums[1] : ans = nums[0]
            else : ans = 0
            p1, p2 = nums[0], nums[1]
        except : return nums[0]

        for n in nums[2:] :
            if p1 != p2 and p2 != n : ans += p2
            p1, p2 = p2, n
        if p1 != p2 : return ans + p2
        return ans