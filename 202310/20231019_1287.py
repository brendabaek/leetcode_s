## https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        dics = {}
        for a in arr :
            try : dics[a] += 1
            except : dics[a] = 1
        return max(dics, key=dics.get)