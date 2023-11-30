## https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        dics = {}
        for num in nums :
            try : dics[num] += 1
            except : dics[num] = 1
        lst = [dics[max(dics)]]
        
        for i in range(max(dics)-1, -1, -1) :
            try : lst.insert(0, lst[0]+dics[i])
            except : lst.insert(0, lst[0])

        for j in range(len(nums)+1) :
            try :
                if j == lst[j] : return j
            except : return -1
        return -1