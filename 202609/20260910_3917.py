## https://leetcode.com/problems/count-indices-with-opposite-parity/

class Solution:
    def countOppositeParity(self, nums: list[int]) -> list[int]:
        eo, ans = [], []
        for num in nums: eo.append(num % 2)
        even, odd = eo.count(0), eo.count(1)
        for c in eo:
            if c == 0:
                even -= 1
                ans.append(odd)
            else:
                odd -= 1
                ans.append(even)
        return ans