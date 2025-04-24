## https://leetcode.com/problems/find-the-xor-of-numbers-which-appear-twice/

class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        l1, l2, ans = [], [], 0
        for num in nums:
            if num not in l1: l1.append(num)
            else: l2.append(num)
        for l in l2: ans ^= l
        return ans