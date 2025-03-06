## https://leetcode.com/problems/most-frequent-even-element/

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        dics = {}
        for num in nums :
            if num % 2 == 1 : continue
            try : dics[num] += 1
            except : dics[num] = 1
        dics = dict(sorted(dics.items()))
        try : return max(dics, key=dics.get)
        except : return -1