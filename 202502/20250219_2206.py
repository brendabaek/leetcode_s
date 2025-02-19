## https://leetcode.com/problems/divide-array-into-equal-pairs/

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        dics = {}
        for num in nums :
            try : del dics[num]
            except : dics[num] = 1
        return dics == {}