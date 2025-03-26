## https://leetcode.com/problems/remove-trailing-zeros-from-a-string/

class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        # num = int(num)
        # while num % 10 == 0 : num = num // 10
        # return str(num)
        
        # return str(int(num[::-1]))[::-1]

        return num.rstrip("0")