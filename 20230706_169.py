## https://leetcode.com/problems/majority-element/

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if nums == None  : return
        dics = {}
        for n in nums :
            if n in dics :  dics[n] += 1
            else : dics[n] = 1
        
        ans = max(dics, key=dics.get)
        return ans