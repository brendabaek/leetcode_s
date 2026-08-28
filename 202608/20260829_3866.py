## https://leetcode.com/problems/first-unique-even-element/

class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        lst1, lst2 = [], []
        for num in nums:
            if num % 2 == 1: continue
            if num not in lst1 and num not in lst2: lst1.append(num)
            elif num in lst1: lst2.append(num)
        for l in lst1:
            if l not in lst2: return l
        return -1