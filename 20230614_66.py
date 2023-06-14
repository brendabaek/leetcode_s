## https://leetcode.com/problems/plus-one/

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        for i in range(len(digits)) :
            if i == 0 : nums = str(digits[i])
            else : nums += str(digits[i])
        
        nums = str(int(nums)+1)
        ans = []

        for j in range(len(nums)) :
            ans.append(int(nums[j]))

        return ans