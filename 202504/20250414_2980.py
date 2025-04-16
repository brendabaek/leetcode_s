## https://leetcode.com/problems/check-if-bitwise-or-has-trailing-zeros/

class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        check = False
        for num in nums:
            if num % 2 == 0:
                if check == False: check = True
                else : return True
        return False