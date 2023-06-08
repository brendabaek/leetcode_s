## https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        cnt = 0
        ln = len(nums)
        
        if ln <= 1 : return ln
        else :
            for i in range(ln-1) :
                if nums[cnt] == nums[cnt+1] :
                    nums.pop(cnt+1)
                    nums.append(0)
                else :
                    cnt +=1
        return cnt+1