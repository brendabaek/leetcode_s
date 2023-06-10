class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        ln = len(nums)
        cnt = 0

        for i in range(ln) :
            if nums[cnt] == val :
                nums.pop(cnt)
            
            else : cnt += 1

        ans = len(nums)
        for j in range(ln-cnt) :
            nums.append('_')
        
        return ans     