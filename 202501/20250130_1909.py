## https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/

class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool :
        p2, p1, check = 0, 0, True
        for i in range(len(nums)) :
            if p1 < nums[i] : p2, p1 = p1, nums[i]
            else :
                if check == False : return False
                if nums[i] <= p2 : check = False
                else : p1, check = nums[i], False
        return True